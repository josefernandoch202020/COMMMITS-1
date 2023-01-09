from django.http import HttpResponse
def jose():
    mensaje={"<h1> bienvenidos</h1>"}
    return HttpResponse(mensaje)