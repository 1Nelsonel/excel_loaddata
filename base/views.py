from http.client import HTTPResponse
from django.shortcuts import render
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
from .models import Employee
import openpyxl

from tablib import Dataset
from .resources import EmployeeResource

# Create your views here.


def home(request):
    employees = Employee.objects.all()

    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        wb = openpyxl.load_workbook(file, read_only=True)
        ws = wb.active
        rows = list(ws.iter_rows(values_only=True))
        headers = rows[0]
        data = rows[1:]
        for row in data:
            obj = Employee()
            for i, field in enumerate(headers):
                setattr(obj, field, row[i])
            obj.save()
        return render(request, 'home.html')
    
    context = {'employees': employees}
    return render(request, 'home.html', context)


def Import_Excel_pandas(request):
   
    return render(request, 'home.html')


def Import_excel(request):
  
  
    return render(request, 'home.html')
