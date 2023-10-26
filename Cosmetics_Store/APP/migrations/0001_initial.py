# Generated by Django 4.2 on 2023-04-23 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('img_url', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField()),
                ('brand', models.CharField(max_length=200, null=True)),
                ('appointment', models.CharField(max_length=200, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.category')),
            ],
        ),
    ]
