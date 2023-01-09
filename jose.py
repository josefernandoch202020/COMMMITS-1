from django.http import HttpResponse
def jose():
    mensaje={"<h1> Hola mis ampres</h1>"}
    return HttpResponse(mensaje)