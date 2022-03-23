# Generated by Django 4.0.3 on 2022-03-22 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gstrepayment', '0007_remove_entry_delayed'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='due_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='OtherTaxes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('created', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('paid', models.BooleanField(default=False)),
                ('tax_payer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-due_date'],
            },
        ),
    ]
