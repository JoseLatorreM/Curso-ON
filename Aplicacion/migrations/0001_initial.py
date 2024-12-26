# Generated by Django 5.0.7 on 2024-10-09 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NCurso', models.CharField(max_length=12)),
                ('Autor', models.CharField(max_length=22)),
                ('Duracion', models.DecimalField(decimal_places=0, max_digits=10)),
                ('Descripcion', models.CharField(max_length=300)),
                ('Total', models.DecimalField(decimal_places=0, max_digits=11)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RutUsu', models.CharField(max_length=12)),
                ('NomUsu', models.CharField(max_length=22)),
                ('ApeUsu', models.CharField(max_length=22)),
                ('EmailUsu', models.CharField(max_length=22)),
                ('Contraseña', models.CharField(max_length=50)),
            ],
        ),
    ]