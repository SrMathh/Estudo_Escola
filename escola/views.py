from escola.models import Estudante,Curso,Matriculas
from escola.serializers import EstudanteSerializer,CursoSerializer, MatriculasSerializer,ListaMatriculasCursoSerializer,ListaMatriculasEstudanteSerializer
from rest_framework import viewsets, generics


class EstudanteViewSet (viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet (viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculasViewSet (viewsets.ModelViewSet):
    queryset = Matriculas.objects.all()
    serializer_class = MatriculasSerializer

class ListaMatriculasEstudante(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matriculas.objects.filter(estudante_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculasCurso(generics.ListAPIView):
    def gat_queryset(self):
        queryset = Curso.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer