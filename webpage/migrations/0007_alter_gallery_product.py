# Generated by Django 5.0.1 on 2024-01-22 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0006_gallery_delete_galery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='product',
            field=models.ImageField(upload_to=''),
        ),
    ]
