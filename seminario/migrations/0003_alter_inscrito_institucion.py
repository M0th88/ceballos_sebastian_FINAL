# Generated by Django 5.1 on 2024-12-17 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminario', '0002_alter_inscrito_institucion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscrito',
            name='institucion',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
