# Generated by Django 4.2.4 on 2023-08-30 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entregable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('fechaDeEntrega', models.DateField()),
                ('entregado', models.BooleanField()),
            ],
        ),
    ]
