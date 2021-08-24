
from django.shortcuts import render
from django.http import HttpResponse

def String_View(request):
    emp = {
        "eno" : 101,
        "ename" : "Srinivas",
        "salary" : 10000
    }
    response = "<h1><font color='red'>Employee number is : {},<br> Employee Name is {},<br> Employeee Salary is {}</font></h1>".\
        format(emp['eno'],emp['ename'], emp["salary"])

    return HttpResponse(response)


import json
def json_view(request):
    emp = {
        "eno": 102,
        "ename": "Virat",
        "salary": 20000
    }
    json_response = json.dumps(emp)

    return HttpResponse(json_response,content_type='application/json')


from django.http import JsonResponse
def json_view2(request):
    emp = {
        "eno": 103,
        "ename": "Rohit",
        "salary": 30000
    }
    return JsonResponse(emp)


