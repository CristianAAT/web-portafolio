from django.shortcuts import render, HttpResponse, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Project

# Create your views here.
def Index(request):
    form = ContactForm()
    Projects = Project.objects.all()

    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phoneNumber = request.POST.get('phoneNumber', '')
            message = request.POST.get('message', '')
            #Send email
            sendMail = EmailMessage(
                "Mensaje de contacto desde web portafolio",
                "De: {} <{}>, telefono:{}\n\nEscribió:\n{}".format(name, email, phoneNumber, message),
                to=['Cristian_AAT@outlook.com']
            )
            try:
                sendMail.send()
                return redirect('/?ok')
            except:
                return redirect('/?fail')

    return render(request, 'Core/index.html', {'form':form, 'Projects':Projects})