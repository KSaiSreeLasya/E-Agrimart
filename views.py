import os, shutil

from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import *
from django.db.models import F


# Create your views here.


cats = prod_category.objects.all()


def home(request):
    d = products.objects.order_by('cat_name')[:12]
    return render(request, 'index.html', {'prod': d, })


def usersignup(request):
    return render(request, 'signup.html')

def addaddr(request):
    return render(request, 'updateaddr.html')

def terms(request):
    return render(request, 'terms.html')

def faqs(request):
    return render(request, 'faqs.html')

def aboutus(request):

    return render(request, 'aboutus.html')




def signupaction(request):
    email = request.POST['email']
    pwd = request.POST['pwd']
    phone = request.POST['phone']
    name = request.POST['name']
    addr = request.POST['addr']

    addrtype = request.POST['addrtype']
    city = request.POST['city']
    zip = request.POST['zip']

    d = users.objects.filter(email__exact=email).count()

    if d > 0:
        return render(request, 'signup.html', {'msg': "Email Already Registered"})
    else:
        d = users(name=name, email=email, pwd=pwd, phone=phone, stz='verification')
        d.save()
        d = users_locations(email=email, addr_type=addrtype, address=addr, zip=zip, city=city)
        d.save()
        
        return render(request, 'msg.html', {'b': True})


def userlogin(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        pwd = request.POST['pwd']
        d = users.objects.filter(email__exact=uid).filter(pwd__exact=pwd).count()

        if d > 0:
            d = users.objects.filter(email__exact=uid)
            c = prod_category.objects.all()

            request.session['useremail'] = uid
            request.session['username'] = d[0].name
            request.session["msg"] = ''

            return render(request, 'user_home.html', {'data': d[0], 'cat': c })

        else:
            return render(request, 'login.html', {'msg': "Login Fail"})

    else:
        return render(request, 'login.html')


def adminlogin(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        pwd = request.POST['pwd']

        if uid == 'admin' and pwd == 'admin':
            request.session['adminid'] = 'admin'
            return render(request, 'admin_home.html')

        else:
            return render(request, 'admin.html', {'msg': "Login Fail"})

    else:
        return render(request, 'admin.html')


def adminhome(request):
    if "adminid" in request.session:

        return render(request, 'admin_home.html')

    else:
        return render(request, 'login.html')


def userlogout(request):
    try:
        del request.session['useremail']
    except:
        pass
    return render(request, 'login.html')


def adminlogout(request):
    try:
        del request.session['adminid']
    except:
        pass
    return render(request, 'admin.html')


def userhome(request):
    if "useremail" in request.session:
        uid = request.session["useremail"]
        d = users.objects.filter(email__exact=uid)
        c = prod_category.objects.all()
        
        msg = request.session["msg"]
        request.session["msg"] = ''
        d = users.objects.filter(email__exact=uid)
        return render(request, 'user_home.html', {'msg': msg, 'data': d[0],  'cat': c})

    else:
        return render(request, 'login.html')


def profile(request):
    if "useremail" in request.session:
        uid = request.session["useremail"]
        d = users.objects.filter(email__exact=uid)
      
        msg = request.session["msg"]
        request.session["msg"] = ''
        return render(request, 'profile.html', {'data': d[0],  'msg': msg})

    else:
        return render(request, 'login.html')


def addcategory(request):
    d = prod_category.objects.all()
    return render(request, 'addcat.html', {'data': d})


def addcataction(request):
    if request.method == 'POST':
        name = request.POST['name']
        d = prod_category(cat_name=name)
        d.save()
    return redirect('addcategory')


def additem(request):
    d1 = prod_category.objects.all()

    name=''
    cost=''
    ava=''

    return render(request, 'additem.html', {'cat': d1,'name':name,'cost':cost,'ava':ava })

def additemaction(request):
    if request.method == 'POST':
        sid = request.session['sid']
        cat = request.POST['cat']
        cat = cat.split("|")
        catname = cat[0]
        cid = cat[1]
        name = request.POST['name']
        cost = request.POST['cost']
        ava = request.POST['ava']
        des = request.POST['des']
        image = request.FILES['itemimage']

        d = products(cat_id=cid, cat_name=catname, prod_name=name, cost=cost, photo=image, availability=ava, sid=sid, sales=0, description=des)

        d.save()

    d1 = prod_category.objects.all()

    return render(request, 'additem.html', {'cat': d1, 'msg': 'Product Added !!'})



def viewproducts(request):
    if request.method == 'POST':
        cat = request.POST['cat']
        sid = request.session['sid']

        d1 = prod_category.objects.all()
        d2 = products.objects.filter(cat_name=cat).filter(sid=sid)
        return render(request, 'viewproducts.html', {'cat': d1, 'prod': d2})
    else:
        d1 = prod_category.objects.all()
        return render(request, 'viewproducts.html', {'cat': d1})


def addstocks(request):
    if request.method == 'POST':
        pid = request.POST['pid']
        stocks = int(request.POST['stocks'])

        products.objects.filter(id=pid).update(availability=F('availability') + stocks)

        d1 = prod_category.objects.all()
        


        return render(request, 'viewproducts.html', {'cat': d1, 'msg': 'Stocks Updated'})
    else:
        pid = request.GET['pid']
        return render(request, 'addstocks.html', {'pid': pid})


def manageaddress(request):
    if request.method == 'POST':
        email = request.session["useremail"]
        addr = request.POST['addr']

        addrtype = request.POST['addrtype']
        city = request.POST['city']
        zip = request.POST['zip']

        d = users_locations(email=email, addr_type=addrtype, address=addr, zip=zip, city=city)
        d.save()
        request.session["msg"] = 'Address Added !! '
        return redirect('userhome')
    else:
        email = request.session["useremail"]
        d = users_locations.objects.filter(email=email)

        return render(request, 'manageaddress.html', {'data': d, 'cat': cats})


def deleteaddress(request):
    if request.method == 'GET':

        addr = request.GET['id']
        d = users_locations.objects.filter(id=addr)
        print(d[0])
        d.delete()

        return redirect('manageaddress')
    else:
        pass

def updateaddress(request):
    if request.method == 'GET':

        id = request.GET['id']
        d = users_locations.objects.filter(id=id)
        
        return render(request, 'updateaddress.html', {'d': d[0]})
    else:
        addr = request.POST['addr']

        addrtype = request.POST['addrtype']
        city = request.POST['city']
        zip = request.POST['zip']


        id = request.POST['id']
        d = users_locations.objects.filter(id=id).update(address=addr, addr_type=addrtype, city=city, zip=zip)
        return redirect('manageaddress')

def uviewproducts(request, cid):
    if "useremail" in request.session:
        cat = cid

        d = products.objects.filter(cat_id=cat).order_by('-sales')
        pid=0
        for d1 in d:
            pid=d1.id
            break
        return render(request, 'uviewproducts.html', {'prod': d, 'cat': cats, 'pid':pid})
    else:
        return redirect('userlogout')


def search(request):
    if "useremail" in request.session:

        name = request.POST['name']
        

        d = products.objects.filter(prod_name__icontains=name)
        return render(request, 'uviewproducts.html', {'prod': d, 'cat': cats})
    else:
        return redirect('userlogout')


def viewsingle(request, pid):
    if "useremail" in request.session:
        pid = pid
        email = request.session["useremail"]
        import random as r
        no = r.randint(1, 7)


        from .Dates import get
        ddate = get(no)

        d = products.objects.filter(id=pid)
        print(d[0].prod_name)
        return render(request, 'viewsingle.html', {'d': d[0], 'cat': cats, 'ddate': ddate})

    else:
        return redirect('userogout')


def addtocart(request):
    email = request.session["useremail"]
    qua = request.POST['qua']
    sid = request.POST['sid']
    pid = request.POST['pid']
    ddate = request.POST['ddate']

    d = products.objects.filter(id=pid)

    d2 = cart(email=email, pid=pid, prod_name=d[0].prod_name, unit_cost=float(d[0].cost), sid=sid,tot_cost=float(d[0].cost) * float(qua), photo=d[0].photo, d_date=ddate, quantity=qua)
    d2.save()
    request.session["msg"] = 'Product Added to Cart !!'
    return redirect('userhome')


def cartview(request):
    if "useremail" in request.session:
        email = request.session["useremail"]

        d = cart.objects.filter(email=email)
        return render(request, 'cartview.html', {'cat': cats, 'cart': d})
    else:
        return redirect('userlogout')


def cartdelete(request, op):
    if request.method == 'GET':

        pid = op
        d = cart.objects.filter(id=pid)
        print(d[0])
        d.delete()

        return redirect('cartview')
    else:
        pass


def payment(request):
    if request.method == 'POST':
        email = request.session["useremail"]

        d = cart.objects.filter(email=email)
        from .RandomGen import get
        oid = int(get())
        for d1 in d:
            d2 = orders(oid=oid, email=email, pid=d1.pid, prod_name=d1.prod_name, unit_cost=d1.unit_cost,
                        tot_cost=d1.tot_cost, photo=d1.photo, d_date=d1.d_date, quantity=d1.quantity, stz='Ordered',
                        progress=25, sid=d1.sid)
            d2.save()

        from .Dates import get
        ddate = get(0)


        request.session["msg"] = 'Purchase Completed !!'
        d = cart.objects.filter(email=email)
        d.delete()
        products.objects.filter(id=d1.pid).update(availability=F('availability') - d1.quantity)
        products.objects.filter(id=d1.pid).update(sales=F('sales') + 1)

        return redirect('userhome')
    else:
        email = request.session["useremail"]
        d = cart.objects.filter(email=email)
        tot = 0.0
        b = True

        for d1 in d:
            tot = tot + d1.tot_cost

        return render(request, 'buy.html', {'tot': tot, 'b': b})


def sellersignup(request):
    if request.method == 'POST':
        empid = request.POST['empid']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        pwd = request.POST['pwd']
        address = request.POST['address']
        stz = 'new'

        d = seller(sid=empid, name=name, email=email, phone=phone, pwd=pwd, address=address, stz=stz)
        d.save()
        return render(request, 'sellersignup.html', {'msg': 'Seller Added Successfully !!'})


    else:

        import random as r
        eid = "SELLER" + str(r.randint(1000, 10000))

        return render(request, 'sellersignup.html', {'empid': eid})


def newsellers(request):
    if "adminid" in request.session:

        d = seller.objects.filter(stz__exact='new')
        return render(request, 'newsellers.html', {'emp': d})
    else:
        return redirect('adminlogout')



def sellerstz(request):
    if "adminid" in request.session:
        id = request.GET['id']
        stz = request.GET['stz']
        seller.objects.filter(id=id).update(stz=stz)
        return redirect('newsellers')
    else:
        return redirect('adminlogout')



def slogin(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        pwd = request.POST['pwd']
        d = seller.objects.filter(sid__exact=uid).filter(pwd__exact=pwd).filter(stz__exact='Accepted').count()

        if d > 0:
            d2 = seller.objects.filter(sid__exact=uid)

            request.session['sid'] = uid
            request.session['sname'] = d2[0].name

            return render(request, 's_home.html', {'data': d2[0]})

        else:
            return render(request, 'sellerlogin.html', {'msg': "Login Fail"})

    else:
        return render(request, 'sellerlogin.html')



def shome(request):
    if "sid" in request.session:

        return render(request, 's_home.html')

    else:
        return render(request, 'sellerlogin.html')


def slogout(request):
    try:
        del request.session['sid']
    except:
        pass
    return render(request, 'sellerlogin.html')


def viewsellers(request):
    if "adminid" in request.session:

        d = seller.objects.all()
        return render(request, 'viewsellers.html', {'data': d})
    else:
        return redirect('adminlogout')


def vieworders(request):
    if "sid" in request.session:

        from .Dates import get
        ddate = get(0)
        sid=request.session['sid']

        o = orders.objects.filter(stz='Ordered').filter(sid=sid)
        c = orders.objects.filter(stz='Confirmed').filter(sid=sid)
        t = orders.objects.filter(d_date=ddate).filter(stz='Confirmed').filter(sid=sid)

        return render(request, 'vieworders.html', {'o': o, 'c': c, 't': t})
    else:
        return redirect('slogout')


def accept(request):
    if request.method == 'GET':
        id = request.GET['id']
        orders.objects.filter(id=id).update(stz='Confirmed', progress=50)
        return redirect('vieworders')


    else:
        pass


def allot(request):
    if request.method == 'GET':

        from .Dates import get
        ddate = get(0)
        oid = request.GET['oid']
        
        orders.objects.filter(id=oid).update(stz='Delivered', progress=100)

        return redirect('vieworders')


    else:
        pass


def uvieworders(request):
    if "useremail" in request.session:

        email = request.session["useremail"]

        d = orders.objects.filter(email=email).order_by('-id') 
        c = prod_category.objects.all()

        return render(request, 'uvieworders.html', {'o': d, 'cat': c})
    else:
        return redirect('userlogout')



def rpay(request):
    if request.method == 'POST':
        email = request.session["useremail"]
        id = request.POST['id']
        oid = request.POST['oid']

        d = orders.objects.filter(oid=oid)

        for d1 in d:
            d2 = orders(oid=0, email=email, pid=d1.pid, prod_name=d1.prod_name, unit_cost=d1.unit_cost,
                        tot_cost=d1.tot_cost, photo=d1.photo, d_date=d1.d_date, quantity=d1.quantity, stz='Ordered',
                        progress=25)
            d2.save()

        request.session["msg"] = 'Purchase Completed !!'
        d = cart.objects.filter(email=email)
        d.delete()
        products.objects.filter(id=d1.pid).update(availability=F('availability') - d1.quantity)

        return redirect('userhome')
    else:
        email = request.session["useremail"]
        id = request.GET['id']
        oid = request.GET['oid']
        tot = 0

        d = orders.objects.filter(oid=oid)
        for d1 in d:
            tot = tot + d1.tot_cost

        return render(request, 'buy2.html', {'tot': tot, 'oid': oid, 'id': id})

def addcoupons(request):
    if request.method == 'POST':
        code = request.POST['code']
        discount = request.POST['discount']
        d = coupons(code=code, discount=discount, stz="Active")
        d.save()

        d=coupons.objects.filter(stz='Active')
        return render(request, 'coupons.html', {'data':d,'msg': "Coupon Added Successfully !! "})


    else:
        d=coupons.objects.filter(stz='Active')
        return render(request, 'coupons.html', {'data':d})

def deletecode(request):
    if request.method == 'POST':
        id = request.POST['id']
        d = coupons.objects.filter(id=id).update(stz='Deactive')
        

        d=coupons.objects.filter(stz='Active')
        return render(request, 'coupons.html', {'data':d,'msg': "Updated !! "})


    else:
        pass



def couponverify(request):
    sid=request.POST['sid']
    coupon=request.POST['coupon']
    amt=float(request.POST['amt'])

    d=coupons.objects.filter(code=coupon).filter(stz='Active')
    if d.exists():
        discount=d[0].discount
        discount=amt*(discount/100)
        amt=amt-discount
        s=cart.objects.filter(sid=sid).update(tot_cost=amt)

        return render(request, 'buy.html', {'tot': amt,  'msg':'Coupon is Applied !!'})
    else:
        return render(request, 'buy.html', {'tot': amt,  'msg':'Coupon is Invalid !!'})


