# Generated by Django 3.2 on 2023-04-19 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_treatment_take'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='range',
            field=models.TextField(blank=True, max_length=300, verbose_name='适用范围'),
        ),
    ]
