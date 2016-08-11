from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from mail_templated import EmailMessage
from .forms import ContactDetails
from .models import contactus
# Create your views here.

def home(request):
    context= RequestContext(request)
    return render_to_response('index.html',{}, context_instance=context )

def contactsave(request):
    context=RequestContext(request)
    if request.method=='POST':
        form = ContactDetails(request.POST)
        if form.is_valid():
            # form.save()
            to="nguruben@gmail.com"
            message = EmailMessage('email/mail.tpl', {}, 'info@i254.co.ke',to=[to])
            message.send()
            print '*******It worked*********'
            return  HttpResponseRedirect('/')

    return render_to_response('index.html', {}, context_instance=context)




