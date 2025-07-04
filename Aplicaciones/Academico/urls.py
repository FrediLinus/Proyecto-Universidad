from django.urls import path
from Aplicaciones.Academico.views import CursoListView

urlpatterns = [
    path('', CursoListView.as_view(), name='gestio_cursos'),  # Ruta para la lista de cursos
    # Puedes agregar más rutas aquí si es necesario
]