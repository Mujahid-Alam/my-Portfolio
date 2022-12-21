from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.
def home(request):
    context = {'home': 'active'}
    return render(request, 'core/home.html',context)

def contact(request):
    if request.method == 'POST':

        # fetch data from form
        name = request.POST.get('name')
        email = request.POST.get('email') 
        subject = request.POST.get('subject') 
        message = request.POST.get('message') 

        print(name)
        print(email)
        print(subject)
        print(message)
        #  set data in object 
        c = Contact()
        c.name = name
        c.email = email
        c.subject = subject
        c.message = message
        
        # save
        c.save()

        return redirect('/')


    context = {'contact': 'active'}
    return render(request, 'core/contact.html',context)