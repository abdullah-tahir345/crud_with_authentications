# Generated by Django 4.2.5 on 2023-10-24 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegStu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('roll', models.IntegerField(null=None)),
                ('phone', models.CharField(max_length=14)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
