from django.urls import path
from administrator import views

app_name= 'administrator'

urlpatterns = [
    path('', views.admin_home,name="admin-home"),
    path('contact-request/',views.contact_request_list,name="contact_request_list"),
    path('contact-request/delete/<int:id>/',views.contact_request_delete,name="contact_request_delete"),
    path('contact-request/detail/<int:id>/',views.contact_request_detail,name="contact_request_detail"),

    path('department/create/', views.DepartmentCreateView.as_view(),name="department_create"),
    path('department/', views.DepartmentListView.as_view(),name="department_list"),
    path('department/update/<int:id>/', views.DepartmentUpdateView.as_view(), name="department_update"),
    path('department/delete/<int:id>/',views.department_delete,name="department_delete"),

    path('package/create/',views.HealthPackageCreateView.as_view(),name="package_create"),
    path('package/',views.HealthPackageListView.as_view(),name="package_list"),
    path('package/update/<int:id>/',views.HealthPackageUpdateView.as_view(),name="package_update"),
    path('package/delete/<int:id>/',views.package_delete,name="package_delete"),

    path('insurance/create/',views.InsuranceCreateView.as_view(),name="insurance_create"),
    path('insurance/',views.InsuranceListView.as_view(),name="insurance_list"),
    path('insurance/update/<int:id>/',views.InsuranceUpdateView.as_view(),name="insurance_update"),
    path('insurance/delete/<int:id>/',views.Insurance_delete,name="insurance_delete"),

]
