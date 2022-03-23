# Generated by Django 4.0.3 on 2022-03-22 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gstrepayment', '0013_alter_entry_sale_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='othertaxes',
            options={},
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='paid',
            new_name='is_paid',
        ),
        migrations.RenameField(
            model_name='othertaxes',
            old_name='paid',
            new_name='is_paid',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='created',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='othertaxes',
            name='created',
        ),
        migrations.RemoveField(
            model_name='othertaxes',
            name='due_date',
        ),
        migrations.AddField(
            model_name='entry',
            name='is_due',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='othertaxes',
            name='is_due',
            field=models.BooleanField(default=True),
        ),
    ]