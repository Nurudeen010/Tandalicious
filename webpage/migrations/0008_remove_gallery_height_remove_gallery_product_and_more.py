# Generated by Django 5.0.1 on 2024-01-22 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0007_alter_gallery_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='height',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='product',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='width',
        ),
        migrations.AddField(
            model_name='gallery',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(null=True, upload_to='gallery/'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
