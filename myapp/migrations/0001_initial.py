# Generated by Django 2.2.1 on 2019-05-08 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('pw', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Start',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.Movie')),
                ('stargazer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.User')),
            ],
        ),
    ]