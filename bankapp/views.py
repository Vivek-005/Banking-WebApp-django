from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from datetime import datetime,date
# Create your views here.

def home(request):
    return render(request,"bankapp/home.html")

def transaction_id_generator():
    today_date = str(date.today()).replace("-", "")
    time_now = str(datetime.now().strftime(
        "%H:%M:%S")).replace(":", "")
    txn_id = "TSF"+today_date + time_now
    return txn_id

def customerdetailpage(request):
    details = customerdetails.objects.all()
    
    context =  { "details":details}

    return render(request,"bankapp/customers.html",context)

def AddCustomerpage(request):
    if request.method=="POST":
        acno=request.POST.get('acno')
        name=request.POST.get('name')
        email=request.POST.get('email')
        amt=request.POST.get('amt')
        send =customerdetails(accno=acno,name=name,email=email,amount=amt)
        send.save()
    return render(request,"bankapp/addcustomer.html")

def Transactions(request):
    senderdetail =customerdetails.objects.all()
    if request.method=='POST':
       semail = request.POST.get('semail')
       samt = request.POST.get('samt')
       remail = request.POST.get('remail')
       print(semail,'  ',samt,'  ',remail)
       samt=int(samt)
       if semail == 'select' or remail=='select' or (semail =='select' and remail =='select') or remail == semail:
           messages.warning(request,"Sender and Reciever are same!!")
           print("Sender and Reciever are same!!")
       elif samt <=0:
           messages.warning(request,"Please Enter Proper Amount!!")
           print("Please Enter Proper Amount!!")
       else:
           for c in senderdetail:
               if c.email == semail:
                   j=semail
                   i=c.accno
                   name=c.name
                   print(j,i,name)
                   if samt>c.amount:
                       messages.warning(request,"Please Check sender balance!!")
                       print("Please Check sender balance!!")
                   break
       for x in senderdetail:
           if x.email == remail:
               raccno = x.accno
               rname = x.name
               rbal = x.amount
               print("Here is the reciver detail")
               print(raccno,"  ",rname,"  ",rbal)
               break                         

       for c in senderdetail:
           if c.email == semail and remail!=semail and remail!='select' and samt<=c.amount and samt>0:
               q1 = transactionhistory(sender = name,reciever=rname,amount=samt)
               acc_bal = c.amount-samt
               q2 = customerdetails.objects.filter(accno=i).update(amount=acc_bal)
               q1.save()
               acc_bal=rbal+samt
               q3=customerdetails.objects.filter(accno=raccno).update(amount=acc_bal)
               messages.success(request,"Transfer Complete")
               print("Transfer Complete")
               return redirect("history")

                 
    return render(request,"bankapp/transaction.html",{"customerdetails":senderdetail})

def sendhistory(request):
    history=transactionhistory.objects.all()
    return render(request,"bankapp/history.html",{'history':history})



'''
def Transactions(request):
    senderdetail =customerdetails.objects.all()
    if request.method=='POST':
       semail = request.POST.get('semail')
       saccno = request.POST.get('saccno')
       samt = request.POST.get('amt')
       remail = request.POST.get('email')
       print(remail)
       try:
           samt=int(samt)
       except:
           print("Enter the Amount")
       for i in senderdetail:
           print(semail)
           if i.email==semail:
               j=i
               accno=i.accno
               break
       for i in senderdetail:
           print(i.email,i.amount,semail)
           if i.email==semail and samt<i.amount and samt > 0:
               amt = i.amount-samt
               ramt = j.amount+samt    
               try:
                   query1 = transactionhistory(name=i.name,email=i.email,debamt=amt,cramt=0,acbal=amt)
                   query2 = customerdetails(accno=i.accno,amount=amt,email=i.email,name=i.name)
                   query3 = transactionhistory(name=j.name,email=j.email,debamt=0,cramt=amt,acbal=ramt)
                   query4 = customerdetails(accno=accno,amt=ramt,email=j.email,name=j.name)
                   query2.save()
                   query1.save()
                   query4.save()
                   query3.save()
                   return render(request,"/transaction")
                   break
               except:
                   print("transaction Failed!!")  
    return render(request,"bankapp/transaction.html",{"customerdetails":senderdetail})
'''