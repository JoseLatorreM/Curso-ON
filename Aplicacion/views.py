
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from Aplicacion.models import usuarios
from Aplicacion.models import cursos
from Aplicacion.models import Unidad
from Aplicacion.models import Comentario
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def VistaUsu(request):
    SacarDatos = usuarios.objects.all()
    return render(request, "Registro.html", {'SacarDatos':SacarDatos})

def mostrar_cursos(request):
    Vcursos = cursos.objects.all()
    return render(request, 'Cursos.html', {'Vcursos': Vcursos})

def MenuVisita(request):
    return render (request, "MenuVisita.html")

def AgregarCursos(request):
    return render(request, "AgregarCursos.html")

def MenuUsuario(request):
    return render(request, 'MenuUsuario.html')

def RegistroU(request):
    return render(request, 'Registro.html')

def IniciarS(request):
    return render(request, 'InicioS.html')

def Soporte(request):
    return render (request, 'Problemas.html')

def ModificarCursos(request):
    return render (request, 'ModificarCursos.html')

def guardarUsu(request):
    if request.method == 'POST':
        rut = request.POST['Rut']
        nombre = request.POST['Nombre']
        apellido = request.POST['Apellido']
        email = request.POST['Email']
        contraseña = request.POST['Contraseña']
        
        SacarDatos = usuarios(
            Rut=rut,
            Nombre=nombre,
            Apellido=apellido,
            Email=email,
            Contraseña=contraseña,
        )

        SacarDatos.save()
        return redirect('IniciarS') 
    return render(request, 'RegistroU.html') 

def login_view(request):
    if request.method == "POST":
        rut = request.POST.get("rut")
        password = request.POST.get("password")

        try:
            user = usuarios.objects.get(Rut=rut)
            if password == user.Contraseña:
                request.session['user_name'] = user.Nombre
                request.session['user_lastname'] = user.Apellido    
                return redirect('MenuUsuario')
            else:
                messages.error(request, "Rut o contraseña incorrectos. Inténtalo de nuevo.")
        except usuarios.DoesNotExist:
            messages.error(request, "Rut o contraseña incorrectos. Inténtalo de nuevo.")
    return render(request, 'InicioS.html')


def GuardarCursos(request):
    if request.method == 'POST':
        cursoc = request.POST['NCurso']
        autor = request.POST['Autor']
        duracion = request.POST['Duracion']
        descripcion = request.POST['Descripcion']
        total = request.POST['Total']
        dificultad = request.POST['Dificultad']
        categoria = request.POST['Categoria']
        desdet = request.POST['DesDet']
        num_unidades = int(request.POST['NumUnidades'])
        imagen_portada = request.FILES.get('ImagenPortada')  

        Vcursos = cursos(
            NCurso=cursoc,
            Autor=autor,
            Duracion=duracion,
            Descripcion=descripcion,
            Total=total,
            Dificultad=dificultad,
            Categoria=categoria,
            DesDet=desdet,
            NumUnidades=num_unidades,
            ImagenPortada=imagen_portada,
        )
        Vcursos.save()
    for i in range(1, num_unidades + 1):
            unidad_nombre = request.POST.get(f'unidades[{i}][nombre]')
            unidad_contenido = request.POST.get(f'unidades[{i}][contenido]')
            unidad_imagen = request.FILES.get(f'unidades[{i}][imagen]')
            if unidad_nombre and unidad_contenido:
                Unidad.objects.create(
                    curso=Vcursos,
                    nombre=unidad_nombre,
                    contenido=unidad_contenido,
                    imagen=unidad_imagen,
                )
    return redirect('mostrar_cursos')

def cerrar_sesion(request):
    request.session.flush()
    return redirect('/')

def detalle_curso(request, curso_id):
    curso = get_object_or_404(cursos, id=curso_id)
    comentarios = Comentario.objects.filter(curso=curso).order_by('-fecha')
    return render(request, 'detalle_curso.html', {'curso': curso, 'comentarios': comentarios})

def realizar_curso(request, curso_id):
    curso = get_object_or_404(cursos, id=curso_id)
    unidades = Unidad.objects.filter(curso=curso)
    return render(request, 'realizar_curso.html', {'curso': curso, 'unidades': unidades})

def eliminar_curso(request, curso_id):
    if request.method == "POST":
        curso = get_object_or_404(cursos, id=curso_id)
        curso.delete()
        messages.success(request, "El curso ha sido eliminado con éxito.")
        return redirect('mostrar_cursos')
    else:
        messages.error(request, "Acción no permitida.")
        return redirect('detalle_curso', curso_id=curso_id)

def modificar_curso(request, curso_id):
    curso = get_object_or_404(cursos, id=curso_id)
    
    if request.method == 'POST':
        cursoc = request.POST['NCurso']
        autor = request.POST['Autor']
        duracion = request.POST['Duracion']
        descripcion = request.POST['Descripcion']
        total = request.POST['Total']
        dificultad = request.POST['Dificultad']
        categoria = request.POST['Categoria']
        desdet = request.POST['DesDet']
        num_unidades = int(request.POST['NumUnidades'])
        imagen_portada = request.FILES.get('ImagenPortada', curso.ImagenPortada)
        
        curso.NCurso = cursoc
        curso.Autor = autor
        curso.Duracion = duracion
        curso.Descripcion = descripcion
        curso.Total = total
        curso.Dificultad = dificultad
        curso.Categoria = categoria
        curso.DesDet = desdet
        curso.NumUnidades = num_unidades
        curso.ImagenPortada = imagen_portada
        curso.save()
        
        for i in range(1, num_unidades + 1):
            unidad_data = request.POST.getlist(f'unidades[{i}][nombre]')
            contenido_data = request.POST.getlist(f'unidades[{i}][contenido]')
            imagen_data = request.FILES.get(f'unidades[{i}][imagen]')
            
            if unidad_data and contenido_data:
                unidad = curso.unidades.all()[i - 1]
                unidad.nombre = unidad_data[0]
                unidad.contenido = contenido_data[0]
                if imagen_data:
                    unidad.imagen = imagen_data
                unidad.save()
        
        return redirect('mostrar_cursos')
    
    else:
        unidades = curso.unidades.all()
        return render(request, 'ModificarCursos.html', {'curso': curso, 'unidades': unidades})
    
def agregar_comentario(request, curso_id):
    curso = get_object_or_404(cursos, id=curso_id)

    if request.method == 'POST':
        contenido = request.POST.get('Comentario')
        Comentario.objects.create(
                contenido=contenido,
                curso=curso,
                usuario=usuarios
            )
        return redirect('detalle_curso')
    else:
        return redirect('IniciarS')