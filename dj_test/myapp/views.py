from django.shortcuts import render
from .models import *

# Create your views here.

def myapp_index(request):
#------------------------
    ls_records = TestModel.objects.all()
    context = {'ls_records':ls_records}
    return render(request, "myapp_index.html",context)