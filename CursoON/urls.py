"""
URL configuration for CursoON project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Aplicacion import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/', views.VistaUsu, name=''),
    path('GuardarUsuario/', views.guardarUsu, name='guardarUsu'),
    path('IniciarS', views.IniciarS, name='IniciarS'),
    path('', views.MenuUsuario, name='MenuUsuario'),
    path('RegistrarUsuario', views.RegistroU, name='RegistroU'),
    path('login', views.login_view, name='login_view'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('GuardarCursos/', views.GuardarCursos, name='GuardarCursos'),
    path('mostrar_cursos/', views.mostrar_cursos, name='mostrar_cursos'),   
    path('AgregarCurso/', views.AgregarCursos, name='AgregarCursos'),   
    path('Soporte', views.Soporte, name='Soporte'),
    path('curso/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    path('realizar_curso/<int:curso_id>/', views.realizar_curso, name='realizar_curso'),
    path('eliminar_curso/<int:curso_id>/', views.eliminar_curso, name='eliminar_curso'),
    path('modificar_curso/<int:curso_id>/', views.modificar_curso, name='modificar_curso'),
    path('agregar_comentario/<int:curso_id>/', views.agregar_comentario, name='agregar_comentario'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)