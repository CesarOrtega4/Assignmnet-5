# Generated by Django 5.0.4 on 2024-04-08 22:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barkyapi', '0004_category_alter_bookmark_date_added_alter_bookmark_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='barkyapi.category'),
        ),
    ]
