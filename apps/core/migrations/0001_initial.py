# Generated by Django 3.1.7 on 2021-04-04 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('description', models.CharField(blank=True, max_length=20, null=True, verbose_name='descrição')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='foto')),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='arquivo')),
            ],
            options={
                'verbose_name': 'foto',
                'verbose_name_plural': 'fotos',
                'ordering': ('-created',),
            },
        ),
    ]
