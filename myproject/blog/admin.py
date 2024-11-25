from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')  # Columnas en la lista
    list_filter = ('author', 'created_date', 'published_date')  # Filtros laterales
    search_fields = ('title', 'text')  # Campo de búsqueda
    date_hierarchy = 'published_date'  # Navegación por fechas
    ordering = ('-created_date',)  # Ordenación por defecto (descendente)

    # Configuración del formulario en el administrador
    fieldsets = (
        ('General', {
            'fields': ('author', 'title', 'text'),
        }),
        ('Dates', {
            'fields': ('created_date', 'published_date'),
        }),
    )


# Register your models here.
