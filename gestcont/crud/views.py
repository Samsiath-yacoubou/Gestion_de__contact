from django.shortcuts import render ,get_list_or_404,redirect
from .models import contact

# Create your views here.
def contact_list(request):
     contacts = contact.objects.all()
     return render (request,'crud/contact_list.html',{'contacts':contacts})

def contact_create(request):
     if request == 'POST':
        contacts = contact(name=request.POST['name'],email=request.POST['email'])
        contacts.save()
        return render(request,'crud/contact_create.html')

def contact_update(request,pk):
    contacts=get_list_or_404(contact,pk=pk)
    if request.method =='POST':
       contacts.name = request.POST['name']
       contacts.email = request.POST['email']
       contacts.phone = request.POST['phone']
       contacts.save()
       
       return render (request,'crud/contact_update.html',{'contacts':contacts})

def contact_delete(request,pk):
    contacts=get_list_or_404(contact,pk=pk)
    if request.method =='POST':
       contact.delete()
       return redirect('contact_list')
       return render(request,'crud/contact_delete.html',{'contacts':contacts})