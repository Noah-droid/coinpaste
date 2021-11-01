from django.shortcuts import render
from .forms import CrypForm
# Create your views here.

def welcome(request):
	cform = CrypForm(request.POST or None)
	if cform.is_valid():
		cform.save()
		cform = CrypForm()
	return render(request,'index.html',{'cform':cform})