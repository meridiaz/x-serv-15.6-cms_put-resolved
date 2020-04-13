from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.template import loader

from .models import Contenido, Comentario

formulario_contenido = """
<br>
<form action="" method="POST">
  Introduce el (nuevo) contenido para esta página: 
  <input type="text" name="valor">
  <input type="submit" name="action" value="Enviar Contenido">
</form>
"""

formulario_comentario = """
<br>
<form action="" method="POST">
  Introduce un nuevo comentario para esta página: 
  <br>Título: <input type="text" name="titulo">
  <br>Cuerpo: <input type="text" name="cuerpo">
  <input type="submit" name="action" value="Enviar Comentario">
</form>
"""

@csrf_exempt
def get_content(request, llave):
    if request.method == "PUT":
        valor = request.body.decode('utf-8')           
    elif request.method == "POST":
        action = request.POST['action']
        if action == "Enviar Contenido":
            valor = request.POST['valor']
    if request.method == "PUT" or (request.method == "POST" and action == "Enviar Contenido"):
        try:
            c = Contenido.objects.get(clave=llave)
            c.valor = valor
        except Contenido.DoesNotExist:
            c = Contenido(clave=llave, valor=valor)
        c.save()
    if request.method == "POST" and action == "Enviar Comentario":
            c = Contenido.objects.get(clave=llave)    
            titulo = request.POST['titulo']
            cuerpo = request.POST['cuerpo']
            q = Comentario(contenido=c, titulo=titulo, cuerpo=cuerpo, fecha=timezone.now())
            q.save()

    contenido = get_object_or_404(Contenido, clave=llave)
    comentarios = contenido.comentario_set.all()
    respuesta = contenido.valor
    for comentario in comentarios:
        respuesta += "<p><b>Título</b>: " + comentario.titulo + "<br><b>Cuerpo</b>: " + comentario.cuerpo + "<br><b>Enviado</b>: " + comentario.fecha.strftime('%Y-%m-%d %H:%M:%S') + "</p>"
    respuesta += formulario_comentario + formulario_contenido
    return HttpResponse(respuesta)


def index(request):
    content_list = Contenido.objects.all()[:5]
    context = {'content_list': content_list}
    return render(request, 'cms/index.html', context)
