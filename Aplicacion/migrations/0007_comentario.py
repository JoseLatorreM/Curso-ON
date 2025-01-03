# Generated by Django 5.0.7 on 2024-12-10 21:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0006_unidad_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='Aplicacion.cursos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplicacion.usuarios')),
            ],
        ),
    ]
