# Generated by Django 3.1.3 on 2020-12-23 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_elements_element_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elements',
            name='filename',
            field=models.ImageField(default=None, upload_to='images'),
        ),
    ]