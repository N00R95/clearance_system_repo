from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _, gettext_noop
from core.utils import approvals

approval_status_options = [
    ('Pending', _('Pending')),
    ('Approved', _('Approved')),
    ('Rejected', _('Rejected')),
]

clearance_status_options = [
    ('Pending for HR initial approval', _('Pending for HR initial approval')),
    ('Pending for other departments approval', _('Pending for other departments approval')),
    ('Pending for HR final approval', _('Pending for HR final approval')),
    ('Approved', _('Approved')),
    ('Rejected', _('Rejected')),
]
clearance_type_options = [
    ('', _('Select Clearance Type')),
    ('Annual Vacation', _('Annual Vacation')),
    ('Compensatory Leave', _('Compensatory Leave')),
    ('End of Services', _('End of Services')),
    ('Commissioning', _('Commissioning')),
    ('Redeployment', _('Redeployment')),
    ('Delegation', _('Delegation')),
]

job_title_options = [
    ('', _('Select your Job Title')),
    (_('others'), (
        ('Administrative', _('Administrator')),
        ('Assistant', _('Assistant')),
        ('Technician', _('Technician')),
        ('Specialist', _('Specialist')),
        ('Senior Specialist', _('Senior Specialist')),
        ('Specialist Consultant', _('Specialist Consultant')),
        ('Pharmacist', _('Pharmacist')),
        ('Senior Pharmacist', _('Senior Pharmacist')),
        ('Consultant Pharmacist', _('Consultant Pharmacist')),
    )),
    (_('Medical Departments'), (
        ('Specialist Doctor', _('Specialist Doctor')),
        ('Consultant Doctor', _('Consultant Doctor')),
        ('Resident', _('Resident')),)),
    (_('Nursing Departments'), (
        ('Health Aide', _('Health Aide')),
        ('Nursing Technician', _('Nursing Technician')),
        ('Specialist Nurse', _('Specialist Nurse')),
        ('Senior Specialist Nurse', _('Senior Specialist Nurse')),
        ('Consultant Specialist Nurse', _('Consultant Specialist Nurse')),

    )),
]
gender_options = [
    ('', _('Select Gender')),
    ('Female', _('Female')),
    ('Male', _('Male')),
]


class User(AbstractUser):
    department = models.ForeignKey('core.Department', on_delete=models.CASCADE)


class Department(models.Model):
    name_ar = models.CharField(max_length=100, null=True, blank=True, unique=True)
    name_en = models.CharField(max_length=100, null=True, blank=True, unique=True)
    parent_department = models.CharField(max_length=100, null=True, blank=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.name_en + " - " + self.name_ar


class Clearance(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    clearance_type = models.CharField(max_length=100, choices=clearance_type_options, null=True, blank=True)
    acknowledgment_number = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(default=timezone.now, blank=True)
    end_date = models.DateField(default=timezone.now, blank=True)
    job_title = models.CharField(max_length=100, choices=job_title_options, null=True, blank=True)
    department = models.ForeignKey('core.Department', on_delete=models.CASCADE)
    employee_number = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=50, choices=gender_options, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    attachment = models.FileField(upload_to='media', null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    classification = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(default='Pending for HR initial approval', max_length=50,
                              choices=clearance_status_options)


class Approval(models.Model):
    clearance = models.ForeignKey('core.Clearance', on_delete=models.CASCADE)
    department = models.ForeignKey('core.Department', on_delete=models.CASCADE)
    status = models.CharField(default='Pending', max_length=50, choices=approval_status_options)
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now, blank=True)
    updated = models.DateTimeField(default=timezone.now, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        # if it is HR request we need to do some extra steps
        if self.department.name_en == "Human Resources":
            self.hr_check()
        # check if this is the last needed approval
        else:
            pending_count = Approval.objects.filter(clearance=self.clearance, status="Pending").count()
            if pending_count == 0 and self.clearance.status == "Pending for other departments approval":
                self.clearance.status = "Pending for HR final approval"
                self.clearance.save()
                human_resources_department = Department.objects.get(name_en="Human Resources")
                Approval.objects.create(clearance=self.clearance, department=human_resources_department, )

    # check if the current status of this request is waiting for HR approval
    def hr_check(self):
        # If the HR rejected the request then reject everything
        if self.status == "Rejected":
            self.clearance.status = "Rejected"
            self.clearance.save()
        # If the status is (Pending for HR initial approval) then create the other approvals
        elif self.clearance.status == "Pending for HR initial approval" and self.status == "Approved":
            self.create_approvals()
            self.clearance.status = "Pending for other departments approval"
            self.clearance.save()
        # If the status is (Pending for HR final approval) then approve the whole clearance
        elif self.clearance.status == "Pending for HR final approval" and self.status == "Approved":
            self.clearance.status = "Approved"
            self.clearance.save()

    def create_approvals(self):
        approvals_list = approvals.get(self.clearance.classification, [])
        for approval in approvals_list:
            department = Department.objects.get(name_en=approval)
            Approval.objects.create(clearance=self.clearance, department=department)
        Approval.objects.create(clearance=self.clearance, department=self.clearance.department)
