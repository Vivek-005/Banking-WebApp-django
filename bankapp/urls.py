from django.urls import path
from . import views

urlpatterns=[
    path('', views.home,name='home'),
    path('customers/',views.customerdetailpage,name='customers'),
    path('addcustomers/',views.AddCustomerpage,name='addcustomer'),
    path('transactions/',views.Transactions,name='transactions'),
    path('history/',views.sendhistory,name='history'),

]