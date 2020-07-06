from django.shortcuts import render
from django.http import HttpResponse

from .models import Subscriber
from .forms import Subscriber_Form

# Create your views here.
def home(request):
  if request.method == 'POST':
    sub_form = Subscriber_Form(request.POST)
    if sub_form.is_valid():
      new_sub = sub_form.save()
  else:
    sub_form = Subscriber_Form()

  context = {'sub_form': sub_form}
  return render(request, 'home.html', context)

def dashboard(request):
  subs = Subscriber.objects.all()
  context = {"subs": subs}
  return render(request, 'dashboard.html', context)