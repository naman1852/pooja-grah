# Generated by Django 3.2.6 on 2022-04-19 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='mobile_no',
            field=models.CharField(max_length=15),
        ),
    ]