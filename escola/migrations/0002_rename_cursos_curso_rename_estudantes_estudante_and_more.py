# Generated by Django 5.1.3 on 2024-11-05 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cursos',
            new_name='Curso',
        ),
        migrations.RenameModel(
            old_name='estudantes',
            new_name='Estudante',
        ),
        migrations.RenameField(
            model_name='estudante',
            old_name='date',
            new_name='data_nascimento',
        ),
    ]
