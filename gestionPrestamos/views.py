#from django.shortcuts import render
import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from gestionPrestamos.models import Libro, Estudiante, prestamo, Devolucion
from django.http import JsonResponse

# Create your views here.

class LibroView(View): 

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)




    '''def get(self,request):
        Libros=list(Libro.objects.values())
        if len(Libros)>0:
            datos={"mensaje":Libros}
        else:
            datos={"mensaje":"No se encontraron Libros."}
        return JsonResponse(datos)'''


    def get (self,request,isbn=""):

        if len(isbn)>0:
            Libros=list(Libro.objects.filter(Isbn=isbn).values())
            if len(Libros)>0:
                datos={"Libro":Libros}
            else:
                datos={"mensaje":"No se encontro el Libro."}
        else:
            Libros=list(Libro.objects.values())
            if len(Libros)>0:
                datos={"mensaje":Libros}
            else:
                datos={"mensaje":"No se encontraron Libros."}
       
        return JsonResponse(datos)


    def post(self,request):
        data=json.loads(request.body)
        libro = Libro(Isbn=data['Isbn'],titulo=data['titulo'],editorial=data['editorial'],autor=data['autor'],no_page=data['no_page'])
        libro.save()
        datos={'mensaje':'libro registrado exitosamente'}
        return JsonResponse(datos)

    def put(self,request,isbn):
        data=json.loads(request.body)
        libro=list(Libro.objects.filter(Isbn=isbn).values())
        if len(libro)>0:
            lib=Libro.objects.get(Isbn=isbn)
            lib.titulo=data["titulo"]
            lib.editorial=data["editorial"]
            lib.autor=data["autor"]
            lib.no_page=data["no_page"]
            lib.save()
            mensaje={"mensaje":"Libro actualizado exitosamente."}
        else:
            mensaje={"mensaje":"No se encontro el Libro."}
        return JsonResponse(mensaje)

    def delete(self,request,isbn):
        libro=list(Libro.objects.filter(Isbn=isbn).values())
        if len(libro)>0:
            lib=Libro.objects.filter(Isbn=isbn).delete()
            mensaje={"mensaje":"Libro Eliminado exitosamente."}
        else:
            mensaje={"mensaje":"No se encontro el Libro."}
        return JsonResponse(mensaje)

class prestamoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request):
        data=json.loads(request.body)
        try:
            lib=Libro.objects.get(Isbn=data["libro"])
            est=Estudiante.objects.get(documento=data["documento"])
            pres=prestamo.objects.create(estudiante=est,libro=lib)
            pres.save()
            mensaje={"mensaje":"Prestamo Registrado."}
        except Libro.DoesNotExist:
            mensaje={"mensaje":"El libro no existe."}
        except Estudiante.DoesNotExist:
            mensaje={"mensaje":"El estudiante no existe."}

        return JsonResponse(mensaje)

class DevolucionView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post (self, request):
        data=json.loads(request.body)
        try:
            pres=prestamo.objects.get(id=data["prestamo"])
            dev=Devolucion.objects.create(prestamo=pres)
            dev.save()
            mensaje={"mensaje":"Devolucion Registrada."}
        except Libro.DoesNotExist:
            mensaje={"mensaje":"Prestamo no existe."}
        except Estudiante.DoesNotExist:
            mensaje={"mensaje":"ya existe una devolucion para este prestamo."}

        return JsonResponse(mensaje)