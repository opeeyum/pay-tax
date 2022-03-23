# Generated by Django 4.0.3 on 2022-03-21 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gstrepayment', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='gst_percent',
            field=models.IntegerField(choices=[(0, 'One'), (5, 'Two'), (12, 'Three'), (18, 'Four'), (28, 'Five')], default=0),
        ),
    ]