# Generated by Django 3.1.4 on 2021-04-16 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='created_by',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='shop',
            name='updated_by',
            field=models.JSONField(default=dict),
        ),
    ]