from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def employee_home(request):
    return render(request, 'Employee/home.html')
def addEmp(request):
    if request.method == 'POST':
        # Process the form data
        print("data received")  
        return redirect('/Employee/home/')
    return render(request, 'Employee/addEmp.html')