# Generated by Django 5.1 on 2024-12-17 22:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscrito',
            name='institucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminario.institucion'),
        ),
    ]
