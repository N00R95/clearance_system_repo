from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from .forms import NewClearanceForm, EmployeeSearchForm, UpdateApprovalForm
from .models import *
from .utils import get_matching_classification


class IndexView(TemplateView):
    template_name = 'core/index.html'


class EmployeeCreateClearance(FormView):
    template_name = 'core/employee/create_clearance.html'
    form_class = NewClearanceForm
    success_url = reverse_lazy("core:index")

    def form_valid(self, form):
        data = form.cleaned_data
        if not data["acknowledgment_number"]:
            data["acknowledgment_number"] = None
        data.update({
            "classification": get_matching_classification(data["job_title"]),
            "department": Department.objects.get(name_en=data["department"]),
        })
        clearance = Clearance.objects.create(**data)
        human_resources_department = Department.objects.get(name_en="Human Resources")
        Approval.objects.create(clearance=clearance, department=human_resources_department, )
        messages.success(self.request, "Clearance Created Successfully")
        return super().form_valid(form)

    def get_success_url(self):
        employee_number = self.get_form().data["employee_number"]
        self.success_url = reverse_lazy("core:employee-clearances", kwargs={'employee_number': employee_number})
        return super().get_success_url()


class EmployeeSearchClearances(FormView):
    template_name = 'core/employee/search_clearances.html'
    form_class = EmployeeSearchForm

    def get_success_url(self):
        employee_number = self.get_form().data["employee_number"]
        self.success_url = reverse_lazy("core:employee-clearances", kwargs={'employee_number': employee_number})
        return super().get_success_url()


class EmployeeClearances(TemplateView):
    template_name = "core/employee/clearances.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee_number = kwargs.get('employee_number', None)
        if employee_number:
            context["clearances"] = Clearance.objects.filter(employee_number=employee_number).all()
        return context


class ManagerApprovals(TemplateView):
    template_name = "core/manager/approvals.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get("search", None)
        department = self.request.user.department
        approvals = Approval.objects.filter(department=department)
        if search:
            approvals = approvals.filter(
                Q(clearance__employee_number__exact=int(search)) | Q(clearance_id=int(search)))
        context.update({
            "approvals": approvals,
            "search": search or ''

        })
        return context


class EmployeeShowClearance(TemplateView):
    template_name = "core/employee/show_clearance.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clearance_number = kwargs.get('clearance_number', None)
        clearance = Clearance.objects.get(id=clearance_number)
        context['clearance'] = clearance
        context['approvals'] = Approval.objects.filter(clearance=clearance).all()
        return context


class EmployeePrintClearance(TemplateView):
    template_name = "core/employee/pdfreport.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clearance_number = kwargs.get('clearance_number', None)
        clearance = Clearance.objects.get(id=clearance_number)
        context['clearance'] = clearance
        context['approvals'] = Approval.objects.filter(clearance=clearance).all()
        return context


class ManagerUpdateApproval(FormView):
    template_name = "core/manager/update_approval.html"
    form_class = UpdateApprovalForm
    success_url = reverse_lazy("core:manager-approvals")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        approval_id = self.kwargs.get('approval_id', None)
        approval = Approval.objects.get(id=approval_id)
        context['approval'] = approval
        context['clearance'] = approval.clearance
        return context

    def form_valid(self, form):
        form.cleaned_data.update({
            "approval_id": self.kwargs.get('approval_id', None)
        })
        form.save()
        messages.success(self.request, "Approval Updated Successfully")
        return super().form_valid(form)
