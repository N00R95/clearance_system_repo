from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from core.models import Department, clearance_type_options, job_title_options, gender_options, approval_status_options, \
    Approval


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class TimePickerInput(forms.TimeInput):
    input_type = 'time'


class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'


class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class EmployeeSearchForm(forms.Form):
    employee_number = forms.IntegerField()


def get_department_options():
    departments = Department.objects.filter(hidden=False).all()
    choices = {}
    for department in departments:
        if department.parent_department not in choices:
            choices[department.parent_department] = tuple()
        choices[department.parent_department] += (
            (department.name_en, department.name_ar + " - " + department.name_en),)
    result = [(key, value) for key, value in choices.items()]
    result.insert(0, ('', 'اختر القسم'))
    return result


class NewClearanceForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'your full name..'}))
    clearance_type = forms.ChoiceField(choices=clearance_type_options)
    acknowledgment_number = forms.CharField(required=False)
    start_date = forms.DateField(widget=DatePickerInput)
    end_date = forms.DateField(widget=DatePickerInput)
    job_title = forms.ChoiceField(choices=job_title_options)
    department = forms.ChoiceField(choices=[])
    employee_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '1200..'}))
    gender = forms.ChoiceField(choices=gender_options)
    nationality = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Saudi..'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '05xxxxxxxx'}))
    attachment = forms.FileField(required=False)
    notes = forms.CharField(widget=forms.Textarea,required=False)
    classification = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["department"].choices = get_department_options()


class UpdateApprovalForm(forms.Form):
    status = forms.ChoiceField(choices=approval_status_options)
    notes = forms.CharField(widget=forms.Textarea, required=False)
    approval_id = forms.CharField(required=False)

    def save(self):
        data = self.cleaned_data
        approval = Approval.objects.get(id=data["approval_id"])
        approval.status = data["status"]
        approval.notes = data["notes"]
        approval.save()
