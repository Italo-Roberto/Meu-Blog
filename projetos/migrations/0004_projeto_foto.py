# Generated by Django 4.0.6 on 2022-08-17 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0003_alter_projeto_tecnologias'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='foto',
            field=models.ImageField(default=1, upload_to='projetos/imagens/'),
            preserve_default=False,
        ),
    ]
