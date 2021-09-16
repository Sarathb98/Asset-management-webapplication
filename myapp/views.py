from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from .models import Register
from .models import Login
from .models import Asset


def myfunc(request):
    return render(request, 'index.html')
    

def login(request):
    return render(request, 'login.html')

def cancel(request):
    return render(request, 'index.html')

def regist(request):
    return render(request, 'register.html')
# Create your views here.
def add(request):
    a = request.POST['name']
    b = request.POST['email']
    c = request.POST['addr']
    d = request.POST['phno']
    e = request.POST['uname']

    data=Register(name=a,email=b,addr=c,phno=d,uname=e)
    data.save()
    f = request.POST['paswd']
    g = request.POST['type']
    data1=Login(uname=e,paswd=f,type=g)
    data1.save()

    return render (request,'index.html')

def save(request):
    try:
        i=request.POST['uname']
        j=request.POST['paswd']
        win=Login.objects.get(uname=i, paswd=j)

        if win.type==1:
            request.session['user']=win.uname
            return render(request,'admin-panel.html')
        elif win.type==0:
            request.session['user']=win.uname
            return render(request, 'user-panel.html')

    except:
        return  render(request,'register.html')


def add_btn(request):
    return render(request, 'add.html')


def asset_data(request):
    h = request.POST['ide']
    i = request.POST['dev']
    j = request.POST['dep']
    k = request.POST['own']
    l = request.POST['loc']
    m = request.POST['sts']

    data3 = Asset(ide=h, dev=i, dep=j, own=k, loc=l, sts=m)
    data3.save()
    return render(request, 'admin-panel.html')


def asset_view(request):
    data=Asset.objects.all()
    return render(request, 'view.html',{'data':data})

def edit(request):
    data = Asset.objects.all()
    return render(request, 'update.html' ,{'data':data})


def asset_edit(request):
    index = request.POST['id']
    data = Asset.objects.get(id=index)
    return render(request, 'edit-delete.html',{'s':data})

def asset_update(request):
    id = request.POST['id']
    p = request.POST['ide']
    r = request.POST['dev']
    s = request.POST['dep']
    t = request.POST['own']
    u = request.POST['loc']
    v = request.POST['sts']

    Asset.objects.filter(id=id).update(ide=p, dev=r, dep=s, own=t, loc=u, sts=v )


    data = Asset.objects.all()
    return render(request, 'update.html', {'data':data})

def del_but(request):
    data = Asset.objects.all()
    return render(request, 'delete.html' ,{'data':data})

def deletee(request):
    index = request.POST['id']
    data = Asset.objects.get(id=index)
    data.delete()
    data = Asset.objects.all()
    return render(request, 'delete.html' ,{'data':data})


def home(request):
    return render(request, 'index.html')

