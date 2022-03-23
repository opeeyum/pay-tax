from django.db import models
from users.models import CustomUser
from datetime import timedelta
from django.utils.timezone import now

# Create your models here.
class Entry(models.Model):
    seller = models.ForeignKey(CustomUser, on_delete = models.CASCADE, verbose_name = "Seller") 
    sale_item = models.CharField("Sale Item", max_length=100, default="Goods")   
    buyer = models.CharField("Buyer GSTIN", max_length=15)
    amount = models.DecimalField("Amt. with GST", decimal_places=2, max_digits=10)
    is_paid = models.BooleanField(default=False)

    # Setting due date of after 10 days
    today_date = now().replace(hour=0, minute=0, second=0, microsecond=0)
    due_date = models.DateField(default = today_date+timedelta(days=10))

    class GST_SLAB(models.IntegerChoices):
        TWO = 5
        THREE = 12
        FOUR = 18
        FIVE = 28
    gst_percent = models.IntegerField("GST Slab",choices= GST_SLAB.choices, default=18)
    
    def __str__(self) -> str:
        return self.seller.username +" " + self.sale_item

    @property
    def cgst(self):
        return (self.amount * self.gst_percent / 200)
    
    @property
    def igst(self):
        if self.seller.gst_num[:2] == self.buyer[:2]:
            return 0
        else:
            return (self.amount * self.gst_percent / 200)
    
    @property
    def sgst(self):
        if self.seller.gst_num[:2] == self.buyer[:2]:
            return (self.amount * self.gst_percent / 200)
        else:
            return 0

class OtherTaxes(models.Model):
    accountant = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="Accountant")
    tax_name = models.CharField('Tax Name', max_length=100, null=True)
    tax_payer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="taxPayer")
    amount = models.DecimalField("Amount", decimal_places=2, max_digits=10)
    is_paid = models.BooleanField(default = False)
    
    # Setting due date of after 10 days
    today_date = now().replace(hour=0, minute=0, second=0, microsecond=0)
    due_date = models.DateField(default = today_date+timedelta(days=10))

    
    def __str__(self) -> str:
        return self.tax_name

