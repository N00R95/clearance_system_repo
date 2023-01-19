from django.urls import path
from . import views, apps

app_name = apps.CoreConfig.name

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # Employee
    path('employee/clearances/create', views.EmployeeCreateClearance.as_view(), name='employee-create-clearance'),
    path('employee/clearances/search', views.EmployeeSearchClearances.as_view(),
         name='employee-search-clearances'),
    path('employee/<int:employee_number>/clearances/', views.EmployeeClearances.as_view(), name='employee-clearances'),
    path('employee/clearances/<int:clearance_number>/', views.EmployeeShowClearance.as_view(),
         name='employee-show-clearance'),
    path('employee/clearances/<int:clearance_number>/print', views.EmployeePrintClearance.as_view(),
         name='employee-print-clearance'),
    # Manager
    path('manager/approvals/', views.ManagerApprovals.as_view(), name='manager-approvals'),
    path('manager/approvals/<int:approval_id>/update', views.ManagerUpdateApproval.as_view(),
         name='manager-update-approval'),

]
