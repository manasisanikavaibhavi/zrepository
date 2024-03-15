# Generated by Django 5.0.1 on 2024-03-13 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('cardname', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=10)),
                ('pay_detail', models.CharField(max_length=16)),
                ('cardno', models.CharField(max_length=20)),
                ('cvc', models.CharField(max_length=12)),
                ('month', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=4)),
                ('amount', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='artistfrom',
            name='image',
            field=models.ImageField(upload_to='image'),
        ),
    ]