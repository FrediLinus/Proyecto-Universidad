from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
from django.views.generic import ListView
# Create your views here.


"""
def home(request):
    return HttpResponse("Hola mundo")
    """

def home(request): 
    #cursoListados = Curso.objects.all()[:2] sirve para limitar la cantidad de cursos que se muestran
    cursoListados = Curso.objects.all()  # Obtiene todos los cursos de la base
    #cursoListados = Curso.objects.all().order_by('nombre')  # Ordena los cursos por nombre
    #cursoListados = Curso.objects.all().order_by('-nombre')  # Ordena los cursos por nombre descendente

    #lista de cursos
    data = {
        'titulo': 'Listado de Cursos',
        'cursos': cursoListados,

    }

    #return render(request, 'gestionCursos.html', {'cursos': cursoListados})
    return render(request, 'gestionCursos.html', data)  # Renderiza la plantilla gestionCursos.html con los datos

class CursoListView(ListView):
    model = Curso 
    template_name = 'gestionCursos.html'  # Nombre de la plantilla a usar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Cursos' # Título que se mostrará en la plantilla
        #print (context)
        return context  # Devuelve el contexto para la plantilla
 