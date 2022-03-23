# Generated by Django 4.0.3 on 2022-03-22 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gstrepayment', '0008_entry_due_date_othertaxes'),
    ]

    operations = [
        migrations.AddField(
            model_name='othertaxes',
            name='accountant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Accountant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='othertaxes',
            name='tax_payer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taxPayer', to=settings.AUTH_USER_MODEL),
        ),
    ]
