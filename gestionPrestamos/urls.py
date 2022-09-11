from django.urls import path

from gestionPrestamos.views import LibroView, prestamoView, DevolucionView

urlpatterns = [
    path('Libros/', LibroView.as_view(), name='Listar'),
    path('Libros/<str:isbn>', LibroView.as_view(), name='Buscar'),
    path('Prestamos/', prestamoView.as_view(), name='prestamo'),
    path('Devolucion/', DevolucionView.as_view(), name='dev')
]