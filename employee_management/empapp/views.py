from django.shortcuts import render
from django.db.models import Q
from .models import Employee

from django.shortcuts import render
from .models import Employee

def search_form(request):
    employees = None
    if request.GET:
        fname = request.GET.get('fname', '')
        lname = request.GET.get('lname', '')
        age = request.GET.get('age', '')

        employees = Employee.objects.all()
        if fname:
            employees = employees.filter(fname__startswith=fname)
        if lname:
            employees = employees.filter(lname__startswith=lname)
        if age:
            employees = employees.filter(age__lte=age)

    return render(request, 'empapp/search_form.html', {'employees': employees})



def search_results(request):
    query = request.GET.get('q')
    lookup_type = request.GET.get('lookup')
    results = None

    if lookup_type == 'startswith':
        results = Employee.objects.filter(Q(fname__startswith=query) | Q(lname__startswith=query))
    elif lookup_type == 'contains':
        results = Employee.objects.filter(Q(fname__contains=query) | Q(lname__contains=query))
    elif lookup_type == 'lte':
        results = Employee.objects.filter(age__lte=query)

    return render(request, 'empapp/search_results.html', {'results': results})
