from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola, mundo. Estás en la página de inicio de tu app llamada calc.")

def add(request, op1, op2):
    return HttpResponse(op1+op2)

def sub(request, op1, op2):
    return HttpResponse(op1-op2)

def multi(request, op1, op2):
    return HttpResponse(op1*op2)

def div(request, op1, op2):
    try:
        result = op1/op2
    except ZeroDivisionError:
        result = "No division by zero allowed!"
    return HttpResponse(result)
