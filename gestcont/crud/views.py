
from django.shortcuts import render, get_object_or_404, redirect
from .models import contact

# Lire tous les contacts
def contact_list(request):
    contacts = contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

# Créer un nouveau contact
def contact_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        contact.objects.create(name=name, email=email, phone=phone)
        return redirect('contact_list')
    return render(request, 'contacts/contact_form.html')

# Modifier un contact
def contact_update(request, pk):
    contact_instance = get_object_or_404(contact, pk=pk)
    if request.method == 'POST':
        contact_instance.name = request.POST['name']
        contact_instance.email = request.POST['email']
        contact_instance.phone = request.POST['phone']
        contact_instance.save()
        return redirect('contact_list')
    return render(request, 'contacts/contact_form.html', {'contact': contact_instance})

# Supprimer un contact
def contact_delete(request, pk):
    contact_instance = get_object_or_404(contact, pk=pk)
    if request.method == 'POST':
        contact_instance.delete()
        return redirect('contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact_instance})
