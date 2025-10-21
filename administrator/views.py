from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from django.urls import reverse_lazy
from hmsapp.models import ContactRequest
from .models import Department,HealthPackage,Insurance
from .forms import DepartmentForm,HealthPackageForm,InsuranceForm

# Simple function-based view
def admin_home(request):
    return render(request,'administrator/home.html')


def contact_request_list(request):
    context={}
    context['contact_request'] = ContactRequest.objects.all() 
    return render(request,'administrator/contact_request/list.html',context)


def contact_request_detail(request,id):
    context={}
    context['object'] = get_object_or_404(ContactRequest,id=id)
    return render(request,'administrator/contact_request/detail.html',context)

def contact_request_delete(request,id):
    contact_request=get_object_or_404(ContactRequest,id=id)
    contact_request.delete()
    return redirect('administrator:contact_request_list')


# #class based view
# class ContactRequestListView(ListView):
#     model=ContactRequest
#     template_name='administrator/contact_request/list.html'
#     context_object_name='contact_request'   by default object_list
#     pk_url_kwarg='id'

# Create your views here.
class DepartmentCreateView(CreateView):

    model = Department
    form_class = DepartmentForm
    template_name = 'administrator/departments/department.html'
    success_url = reverse_lazy('administrator:department_list')


class DepartmentListView(ListView):
    model=Department
    template_name= 'administrator/departments/list.html'



class DepartmentUpdateView(UpdateView):

    model = Department
    form_class = DepartmentForm
    template_name = 'administrator/departments/department.html'
    pk_url_kwarg='id'
    success_url = reverse_lazy('administrator:department_list')



def department_delete(request,id):
    department=get_object_or_404(Department,id=id)
    department.delete()
    return redirect("administrator:department_list")

# Health Package

class HealthPackageCreateView(CreateView):
     model = HealthPackage
     form_class=HealthPackageForm
     template_name='administrator/health_package/package.html'
     success_url = reverse_lazy('administrator:package_list')


class HealthPackageListView(ListView):

    model = HealthPackage
    template_name= 'administrator/health_package/list.html'


class HealthPackageUpdateView(UpdateView):
     model = HealthPackage
     form_class=HealthPackageForm
     template_name='administrator/health_package/package.html'
     pk_url_kwarg='id'
     success_url = reverse_lazy('administrator:package_list')

def package_delete(request,id):
    package=get_object_or_404(HealthPackage,id=id)
    package.delete()
    return redirect("administrator:package_list")


# Insurance
class InsuranceCreateView(CreateView):
    model =Insurance
    form_class=InsuranceForm
    template_name='administrator/insurance/insurance.html'
    success_url = reverse_lazy('administrator:insurance_list')

class InsuranceListView(ListView):

    model = Insurance
    template_name= 'administrator/Insurance/list.html'


class InsuranceUpdateView(UpdateView):
     model = Insurance
     form_class=InsuranceForm
     template_name='administrator/insurance/insurance.html'
     pk_url_kwarg='id'
     success_url = reverse_lazy('administrator:insurance_list')

def Insurance_delete(request,id):
    insurance=get_object_or_404(Insurance,id=id)
    insurance.delete()
    return redirect("administrator:insurance_list")

