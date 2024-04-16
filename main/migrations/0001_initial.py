# Generated by Django 3.2.6 on 2022-04-18 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Puja',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nameOfPuja', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mobile_no', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('dateOfPuja', models.DateTimeField()),
                ('total_pay', models.CharField(max_length=50)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pujaName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.puja')),
            ],
        ),
    ]