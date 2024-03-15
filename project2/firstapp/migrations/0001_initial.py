# Generated by Django 5.0.1 on 2024-02-01 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empId', models.IntegerField()),
                ('name', models.CharField(max_length=15)),
                ('course', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=10)),
            ],
        ),
    ]
