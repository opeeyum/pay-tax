from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name='home'),

    path("add_entry/", views.add_entry, name='add_entry'),
    path("edit_entry/<str:pk>/", views.edit_entry, name='edit_entry'),
    path("delete_entry/<str:pk>/", views.delete_entry, name='delete_entry'),

    path("filter_entry/", views.filter_entry, name="filter_entry"),

    path("add_other_tax/", views.add_other_tax, name="add_other_tax"),
    path("edit_other_tax/<str:pk>/", views.edit_other_tax, name='edit_other_tax'),
    path("delete_other_tax/<str:pk>/", views.delete_other_tax, name='delete_other_tax'),

    path("pay_sales_tax/<str:pk>/", views.pay_sales_tax, name="pay_sales_tax"),
    path("pay_other_tax/<str:pk>/", views.pay_other_tax, name="pay_other_tax"),
    

]
