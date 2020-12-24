# Generated by Django 3.1.3 on 2020-12-17 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20201217_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mluser',
            name='labels_correct',
            field=models.CharField(blank=True, default=0, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mluser',
            name='labels_done',
            field=models.CharField(blank=True, default=0, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mluser',
            name='labels_incorrect',
            field=models.CharField(blank=True, default=0, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mluser',
            name='labels_selected',
            field=models.CharField(blank=True, default=0, max_length=1000, null=True),
        ),
    ]