# Generated by Django 4.1.2 on 2022-11-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0004_project_linku'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('subject', models.TextField(blank=True)),
            ],
        ),
    ]