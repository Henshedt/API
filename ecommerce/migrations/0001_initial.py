# Generated by Django 3.2.8 on 2021-10-13 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comprador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('endereco', models.CharField(max_length=300)),
                ('cep', models.CharField(max_length=8)),
            ],
        ),
    ]