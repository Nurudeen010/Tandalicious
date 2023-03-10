# Generated by Django 4.1.7 on 2023-02-21 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tanda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('complaintType', models.CharField(choices=[('issue with staff', 'ISSUE WITH STAFF'), ('issue with food', 'ISSUE WITH FOOD'), ('both', 'BOTH')], default='issue with staff', max_length=50)),
                ('complaintDetails', models.TextField()),
                ('recommendation', models.TextField(blank=True)),
            ],
        ),
    ]
