# Generated by Django 5.0.1 on 2024-01-24 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0011_alter_tanda_complaintdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tanda',
            name='complaintDetails',
            field=models.TextField(default='Write your complaints here', max_length=200),
        ),
        migrations.AlterField(
            model_name='tanda',
            name='recommendation',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
