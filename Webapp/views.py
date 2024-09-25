from django.shortcuts import render,redirect
from Backend.models import productdb,categorydb
from Webapp.models import contactdb
from Webapp.models import Registerdb
from django.contrib import messages
from Webapp.models import cartdb
from Webapp.models import Orderdb
import razorpay

# Create your views here
def homepage(request):
    cat=categorydb.objects.all()
    return render(request,"Home.html",{'category':cat})
def aboutpage(request):
    cat = categorydb.objects.all()
    return render(request,"about.html",{'category':cat})

def contactpage(request):
    cat = categorydb.objects.all()
    return render(request,"contact.html",{'category':cat})
def products(request):
    pro=productdb.objects.all()
    cat = categorydb.objects.all()
    return render(request,"ourproducts.html",{'products':pro,'category':cat})

def save_contact(request):
    if request.method=="POST":
        cn=request.POST.get('cname')
        ce=request.POST.get('cemail')
        cs=request.POST.get('csubject')
        cm=request.POST.get('cmessage')
        cp=request.POST.get('cphone')
        obj=contactdb(CONTACTNAME=cn,CONTACTEMAIL=ce,CONTACTSUBJECT=cs,CONTACTMESSAGE=cm,CONTACTPHONE=cp)
        obj.save()
        return redirect(contactpage)

def filtered_products(request,cat_name):
    cat = categorydb.objects.all()
    data=productdb.objects.filter(CATEGORY=cat_name)
    return render(request,"products_filtered.html",{'data':data,'category':cat})

def single_product(request,pro_id):
    cat = categorydb.objects.all()
    data=productdb.objects.get(id=pro_id)
    return render(request,"single_product.html",{'data':data,'category':cat})

def registration_page(request):
        return render(request,"Register.html")


def save_registration_page(request):
    if request.method == "POST":
        na=request.POST.get('rname')
        em=request.POST.get('remail')
        pa = request.POST.get('rpassword')
        cpa = request.POST.get('rconfirmpassword')
        obj=Registerdb(REGISTERNAME=na,REGISTEREMAIL=em,REGISTERPASSWORD=pa,REGISTERCONFIRMPASSWORD=cpa)
        if Registerdb.objects.filter(REGISTERNAME=na).exists():
            messages.warning(request,"Registername already exists")
            return redirect(registration_page)
        elif Registerdb.objects.filter(REGISTEREMAIL=em).exists():
            messages.warning(request,"Email already exists")
            return redirect(registration_page)
        else:
            obj.save()
            messages.success(request,"Registerd successfully")
        return redirect(registration_page)




def User_login(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        pswd = request.POST.get('upassword')
        if Registerdb.objects.filter(REGISTERNAME=un,REGISTERPASSWORD=pswd).exists():
            request.session['REGISTERNAME']=un
            request.session['REGISTERPASSWORD']=pswd
            messages.success(request,"login successfully..")
            return redirect(homepage)
        else:
            messages.error(request, "login failed")
            return redirect(registration_page)
    else:
        messages.warning(request, "user not found")
        return redirect(registration_page)
def user_logout(request):
    del request.session['REGISTERNAME']
    del request.session['REGISTERPASSWORD']
    messages.success(request, "logout successfully..")
    return redirect(homepage)

#cart save (single_product_page)
def save_cart(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pn=request.POST.get('productname')
        qn=request.POST.get('quantity')
        tr=request.POST.get('totalprice')
        obj=cartdb(USERNAME=un,PRODUCTNAME=pn,QUANTITY=qn,TOTALPRICE=tr)
        obj.save()
        messages.success(request, "item saved")
        return redirect(homepage)
def cart_page(request):
    cat = categorydb.objects.all()
    data=cartdb.objects.filter(USERNAME=request.session['REGISTERNAME'])
    subtotal=0
    shipping_charge=0
    total=0
    for d in data:
        subtotal=subtotal+d.TOTALPRICE
        if subtotal>=500:
            shipping_charge=50
        else:
            shipping_charge=100
        total=subtotal+shipping_charge
    return render(request,"cart.html",{'data':data,'category':cat,'subtotal':subtotal,'total':total,'shipping_charge':shipping_charge})
def delete_item(request,p_id):
    x=cartdb.objects.filter(id=p_id)
    x.delete()
    messages.success(request, "item removed")
    return redirect(cart_page)
def user_login_page(request):
    return render(request,"userlogin.html")
def checkout_page(request):
    cat = categorydb.objects.all()
    products = cartdb.objects.filter(USERNAME=request.session['REGISTERNAME'])
    subtotal = 0
    shipping_charge = 0
    total_amount = 0
    for i in products:
        subtotal = subtotal + i.TOTALPRICE
        if subtotal >= 500:
            shipping_charge = 50
        else:
            shipping_charge = 100
        total_amount = subtotal + shipping_charge


    return render(request,"checkout.html",{'products':products,'shipping_charge':shipping_charge,'subtotal':subtotal,'total_amount':total_amount,'category':cat})

def save_billingaddress(request):
    if request.method=="POST":
        na=request.POST.get('bname')
        em = request.POST.get('bemail')
        ad = request.POST.get('baddress')
        ph = request.POST.get('bphone')
        pr = request.POST.get('bprice')
        me = request.POST.get('bill')
        obj=Orderdb(BILLINGNAME=na,BILLINGEMAIL=em,BILLINGADDRESS=ad,BILLINGPHONE=ph,BILLINGPRICE=pr,BILLINGMESSAGE=me)
        obj.save()
        return redirect(paymentpage)
def paymentpage(request):
    #retrieve the orderdb object with the specified id
    customer=Orderdb.objects.order_by('-id').first()

    #get the payment amount of the specified customer
    payy=customer.BILLINGPRICE

    #convert the amount to paisa(smallest currency unit)
    amount=int(payy*100)

    #convert amount to string for printing
    payy_str=str(amount)

    #printingeach character of the payment amount
    for i in payy_str:
        print(i)
    if request.method=="POST":
        order_currency='INR'
        client=razorpay.Client(auth=('rzp_test_klfWwvjaFXjXmC','s9P7dwOwYckK352FfRJOXIRV'))
        payment=client.order.create({'amount':amount,'currency':order_currency,'payment_capture':'1'})
    return render(request,"payment.html",{'customer':customer,'payy_str':payy_str})

