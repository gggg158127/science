# Generated by Django 3.2 on 2023-04-19 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='recommend',
            field=models.TextField(blank=True, max_length=500, verbose_name='推荐处方'),
        ),
    ]