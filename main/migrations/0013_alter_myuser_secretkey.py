# Generated by Django 3.2.6 on 2022-05-01 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_myuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='secretKey',
            field=models.IntegerField(),
        ),
    ]