# Generated by Django 4.2.4 on 2023-09-04 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_project_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
