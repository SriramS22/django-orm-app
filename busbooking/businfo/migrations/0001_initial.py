# Generated by Django 3.1.1 on 2022-12-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('Busno', models.IntegerField(help_text='Busno', primary_key=True, serialize=False)),
                ('driver', models.CharField(max_length=100)),
                ('From', models.CharField(max_length=100)),
                ('To', models.CharField(max_length=100)),
                ('noofseats', models.IntegerField()),
            ],
        ),
    ]
