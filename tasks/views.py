from django.http import HttpResponse #libreria para dar respuestas para dar respuestas http

def home(request):
    return HttpResponse("hola, esta es mi primera aplicacion")