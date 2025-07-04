from django.contrib import admin
from .models import Curso, Docente


# Register your models here.
#admin.site.register(Curso)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    # Configuración del modelo Curso en el panel de administración
    # Permite editar el modelo Curso desde el panel de administración
    list_display = ('id', 'datos', 'creditos') # lista de campos a mostrar en la lista de cursos

    """
    fieldsets = (
        (None, {
            'fields': ('nombre',)  # Campos a mostrar en el formulario de edición
        }),
        ('Advanced options', {
            'classes': ('collapse','wide','extrapretty'),  # Opciones avanzadas que se pueden colapsar
            'fields': ('creditos',)  # Campos adicionales a mostrar en el formulario de
        }),
    )
    """
    def datos(self,obj):
        return obj.nombre.upper()  # Método para mostrar el nombre del curso en mayúsculas
    

    

    datos.short_description = 'Nombre del Curso'  # Título de la columna en el panel de administración
    datos.empty_value_display = 'Sin Nombre' # Valor a mostrar si el campo está vacío
    datos.admin_order_field = 'nombre' # Permite ordenar por el campo 'nombre' en el panel de administración
#admin.site.register(Curso, CursoAdmin)
admin.site.register(Docente)