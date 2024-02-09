# Generated by Django 4.2.1 on 2024-02-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceProject', '0004_alter_carrinhodecompras_usuario'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('nome', 'sobrenome'), name='nome_sobrenome_unico'),
        ),
    ]