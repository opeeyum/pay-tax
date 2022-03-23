from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPE = (
        ('TP', 'Tax Payer'),
        ('TA', 'Tax Accountant'),
    )

    user_type = models.CharField("Role", max_length=2, choices=USER_TYPE, default='TP')
    gst_num = models.CharField("GSTIN", max_length=15)


