from rest_framework import serializers
from escola.models import Estudante,Curso,Matriculas

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','cpf','data_nascimento','celular']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matriculas
        exclude = []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matriculas
        fields = ['curso', 'periodo']
        def get_periodo(self,obj):
            return obj.get_periodo_display()
        
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')
    class Meta:
        model = Matriculas
        fields = ['estudante_nome']
