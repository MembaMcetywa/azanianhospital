# Generated by Django 3.2.5 on 2021-07-03 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azania', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]