# Generated by Django 4.1.7 on 2023-04-15 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applciation', '0005_alter_project_client_alter_project_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(related_name='projects', to='applciation.user'),
        ),
    ]
