# Generated by Django 4.0.3 on 2022-03-22 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gstrepayment', '0005_alter_entry_amount_alter_entry_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='delayed',
            field=models.BooleanField(default=False),
        ),
    ]