# Generated by Django 3.1.3 on 2020-12-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_projectsdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsdetail',
            name='project_ID',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='projectsdetail',
            name='project_Work_type',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='projectsdetail',
            name='project_description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='projectsdetail',
            name='project_points',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
