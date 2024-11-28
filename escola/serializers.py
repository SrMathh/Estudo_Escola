from rest_framework import serializers
from escola.models import Estudante,Curso,Matriculas
from escola.validators import cpf_invalido, nome_invalido,celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','cpf','data_nascimento','celular']

    def validate(self,dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ser real!'})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome só pode ter letras'})
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'celular':'O celular precisa ter 13 dígitos e sequir formato xx xxxxx-xxxx'})
        return dados
    
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
