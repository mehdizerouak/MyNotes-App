# Generated by Django 4.2.1 on 2023-07-31 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyNotesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='Title',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.CharField(max_length=2000),
        ),
    ]