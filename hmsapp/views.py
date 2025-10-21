from django.shortcuts import render,HttpResponse,redirect

from django.views.generic import View,CreateView
from . import forms


# Create your views here.

def home(request):
    return render(request,'user/home.html')



def about(request):
    return render(request,'user/about.html')


# function based views
def contact(request):
   
    context={}
    if request.method=='GET':
      context={
        'form': forms.ContactForm()
      }
      return render(request,'user/contact.html',context=context)

    elif request.method=='POST':
        context['form'] = forms.ContactForm(request.POST)
        if context['form'].is_valid():
          return HttpResponse("Hello World")
        return render(request,'user/contact.html',context)
        
#class based view
class ContactViewBasic(View):

    def get(self,request):
        return render(request,'user/contact.html')



class ContactCreateView(CreateView):
    
    template_name = 'user/contact.html'
    form_class = forms.ContactForm
    success_url='/'

