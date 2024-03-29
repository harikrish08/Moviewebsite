# Generated by Django 4.2.7 on 2024-02-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=250)),
                ('actors', models.TextField()),
                ('desc', models.TextField()),
                ('year', models.IntegerField()),
                ('rel_d', models.DateField()),
                ('t_link', models.URLField(max_length=500)),
                ('img', models.ImageField(default='null', upload_to='poster')),
            ],
        ),
    ]
