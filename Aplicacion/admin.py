from django.contrib import admin
from .models import usuarios, cursos, Unidad, Comentario

admin.site.register(usuarios)
admin.site.register(cursos)
admin.site.register(Unidad)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('curso', 'usuario', 'fecha')
    search_fields = ('contenido', 'usuario__username', 'curso__NCurso')