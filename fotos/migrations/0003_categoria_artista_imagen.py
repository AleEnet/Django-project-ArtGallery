# Generated by Django 4.1.4 on 2022-12-14 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fotos", "0002_alter_artista_categoria_alter_artista_descripcion"),
    ]

    operations = [
        migrations.AddField(
            model_name="categoria_artista",
            name="imagen",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
