# Generated by Django 3.1.3 on 2020-12-23 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20201223_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elements',
            name='project_ID',
        ),
        migrations.AddField(
            model_name='elements',
            name='project_ID',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.projectsdetail'),
        ),
    ]
