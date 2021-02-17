from django.shortcuts import render
from django.conf import settings                                                                                                                                                       
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect

import requests

from .models import Talking
from .forms import TalkingForm


# form view
def talking_view(request):
    if request.method == 'POST':
        form = TalkingForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            api_key = form.cleaned_data['api_key']
            recepients = form.cleaned_data['recepients']
            message = form.cleaned_data['message']
            sender_id = form.cleaned_data['sender_id']
            
            form.save()
            return HttpResponseRedirect('/core/safaricom_report/')

    else:
        form = TalkingForm()

    context = {'form': form}
    return render(request, "core/send_sms.html", context)


# def safaricom_report(request):
#     context = {}
#     return render(request, "core/report.html", context)


def safaricom_report(request):
    # response = requests.get('').json()
    return render(request, "core/report.html", {})