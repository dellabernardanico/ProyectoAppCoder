from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Curso, Profesor
from .forms import CursoFormulario, ProfesorFormulario

# Create your views here.

def curso(req, nombre, camada):

    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f"""
    <p>Curso: {curso.nombre} - Camada: {curso.camada} creado con exito</p>
    """)

def listar_cursos(req):

    lista = Curso.objects.all()

    return render(req, "lista_cursos.html", {"lista_cursos": lista})


def inicio(req):

    return render(req, "inicio.html")

def cursos(req):

    return render(req, "cursos.html")

def profesores(req):

    return render(req, "profesores.html")

def estudiantes(req):

    return render(req, "estudiantes.html")

def entregables(req):

    return render(req, "entregables.html")

def cursoFormulario(req):

    print('method', req.method)
    print('POST', req.POST)
    
    if req.method == 'POST':

        miFormulario = CursoFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            curso = Curso(nombre=data["curso"], camada=data["camada"])
            curso.save()

            return render(req, "inicio.html")
    else:

        miFormulario = CursoFormulario()
        return render(req, "cursoFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(req):
   
    return render(req, "busquedaCamada.html")

def buscar(req: HttpRequest):

    if req.GET["camada"]:
        camada = req.GET["camada"]
        try:
            cursos = Curso.objects.filter(camada__icontains=camada)
            if cursos:
                return render(req, "resultadosBusqueda.html", {"cursos": cursos})
            else:
                return HttpResponse('No se encontraron cursos para la camada especificada.')
        except Curso.DoesNotExit:
            return HttpResponse('No se encontraron cursos para la camada especificada.')
    else:
        return HttpResponse(f'Debe agregar un numero de camada')

def profesorFormulario(req):

    if req.method == 'POST':
        
        miFormulario = ProfesorFormulario(req.POST)
        
        print(miFormulario)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            profesor = Profesor (nombre=data["nombre"], apellido=data["apellido"],
            email=data["email"], profesion=data["profesion"])

            profesor.save()

            return render(req,"profesorFormulario.html")
        
    else:
        miFormulario= ProfesorFormulario()

    return render(req, "profesorFormulario.html", {"miFormulario":  miFormulario})

def listar_profesores(req):

    lista = Profesor.objects.all()

    return render(req, "lista_profesores.html", {"lista_profesores": lista})
