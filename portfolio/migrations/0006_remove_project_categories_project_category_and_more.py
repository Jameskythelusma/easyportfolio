# Generated by Django 4.2.4 on 2023-09-05 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_project_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='categories',
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('design', 'Design'), ('programming', 'Programming'), ('fitness', 'Fitness'), ('health', 'Health')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
