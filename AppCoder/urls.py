from django.urls import path
from .views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', listar_cursos, name="ListaCursos"),
    path('lista-profesores/', listar_profesores, name="ListaProfesores"),
    path('', inicio, name="Inicio"),
    path('cursos/', cursos, name="Cursos"),
    path('profesores/', profesores, name="Profesores"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('entregables/', entregables, name="Entregables"),
    path('curso-formulario/', cursoFormulario, name="CursoFormulario"),
    path('busqueda-camada/', busquedaCamada, name="BusquedaCamada"),
    path('buscar/', buscar, name="Buscar"),
    path('profesor-formulario/', profesorFormulario, name="ProfesorFormulario"),
    path('estudiante-formulario/', estudianteFormulario, name="EstudianteFormulario"),
]