# Generated by Django 4.1.4 on 2022-12-15 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("fotos", "0005_galeria_imagen_obra_imagen"),
    ]

    operations = [
        migrations.AddField(
            model_name="galeria",
            name="direccion",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="obra",
            name="ano",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="obra",
            name="artista",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="fotos.artista",
            ),
        ),
        migrations.AddField(
            model_name="obra",
            name="galeria",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="fotos.galeria",
            ),
        ),
        migrations.AddField(
            model_name="obra",
            name="precio",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="obra",
            name="tipo_de_artista",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="fotos.categoria_artista",
            ),
        ),
        migrations.AddField(
            model_name="obra",
            name="vendido",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
