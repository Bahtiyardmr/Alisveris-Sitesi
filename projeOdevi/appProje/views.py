from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
# <--------------------------------------------------------------------------- ('_') INDEXS ('_') ------------------------------------------------------------------------>
def index(request):
    cards = Card.objects.all().order_by('-id')
    cards_r = Card.objects.all()
    category=Categori.objects.all()
    pagatitle='Anasayfa'
    userinfo=''
    if request.user.is_authenticated:
     userinfo = Userinfo.objects.get(user=request.user.id)
    
    query=request.GET.get('q')
    if query:
        cards = Card.objects.filter(  Q(title__icontains=query) | Q(text__icontains=query)).distinct()
    
    context = {
        'cards': cards,
        'card_r': cards_r,
        'category': category,
        'pagatitle': pagatitle,
        'userinfo': userinfo
        
    }
    return render(request,'index.html',context)

# <--------------------------------------------------------------------------- ('_') ELEKTORNIK ('_') ------------------------------------------------------------------------>
def Elektronik(request):
    cards = Card.objects.all().order_by('-id')
    pagatitle = 'Elektronik'
    userinfo = ''
    if request.user.is_authenticated:
     userinfo = Userinfo.objects.get(user=request.user.id)
    
    query = request.GET.get('q')
    if query:
        cards = Card.objects.filter(Q(title__icontains=query) | Q(text__icontains=query)).distinct()
    context = {
        'cards': cards,
        'pagatitle': pagatitle,
        'userinfo': userinfo,
    }
    return render(request,'elektronik.html',context)

# <--------------------------------------------------------------------------- ('_') EV ('_') ------------------------------------------------------------------------>
def Ev(request):
    cards = Card.objects.all().order_by('-id')
    pagatitle='Ev'
    userinfo = ''
    if request.user.is_authenticated:
     userinfo = Userinfo.objects.get(user=request.user.id)
    
    query = request.GET.get('q')
    if query:
        cards = Card.objects.filter(Q(title__icontains=query) | Q(text__icontains=query)).distinct()
        
    context = {
        'cards': cards,
        'pagatitle': pagatitle,
        'userinfo': userinfo
    }
    return render(request,'ev.html',context)
# <--------------------------------------------------------------------------- ('_') ANNE ('_') ------------------------------------------------------------------------>


def Anne(request):
    cards = Card.objects.all().order_by('-id')
    pagatitle='Anne'
    
    userinfo = ''
    if request.user.is_authenticated:
     userinfo = Userinfo.objects.get(user=request.user.id)
     
    query = request.GET.get('q')
    if query:
        cards = Card.objects.filter(Q(title__icontains=query) | Q(text__icontains=query)).distinct()

    context = {
        'cards': cards,
        'pagatitle': pagatitle,
        'userinfo': userinfo
    }
    return render(request, 'anne.html', context)
# <--------------------------------------------------------------------------- ('_') SPOR ('_') ------------------------------------------------------------------------>


def Spor(request):
    cards = Card.objects.all().order_by('-id')
    pagatitle='Spor'
    
    userinfo=''
    if request.user.is_authenticated:
     userinfo = Userinfo.objects.get(user=request.user.id)
     
    
    query = request.GET.get('q')
    if query:
        cards = Card.objects.filter(Q(title__icontains=query) | Q(text__icontains=query)).distinct()
        
    context = {
        'cards': cards,
        'pagatitle': pagatitle,
        'userinfo': userinfo
    }
    return render(request, 'spor.html', context)
# <--------------------------------------------------------------------------- ('_') KOZMETIK ('_') ------------------------------------------------------------------------>


def Kozmetik(request):
    cards = Card.objects.all().order_by('-id')
    pagatitle='Kozmetik'
    userinfo = ''
    
    if request.user.is_authenticated:
     userinfo = Userinfo.objects.get(user=request.user.id)
    
    query = request.GET.get('q')
    if query:
        cards = Card.objects.filter( Q(title__icontains=query) | Q(text__icontains=query)).distinct()

    context = {
        'cards': cards,
        'pagatitle': pagatitle,
        'userinfo': userinfo
    }
    return render(request, 'kozmetik.html', context)
# <--------------------------------------------------------------------------- ('_') SUPER ('_') ------------------------------------------------------------------------>


def Super(request):
    cards = Card.objects.all().order_by('-id')
    pagatitle='Super Market'
    userinfo = ''
    if request.user.is_authenticated:
     userinfo = Userinfo.objects.get(user=request.user.id)
    
    query = request.GET.get('q')
    if query:
        cards = Card.objects.filter(Q(title__icontains=query) | Q(text__icontains=query)).distinct()

    context = {
        'cards': cards,
        'pagatitle': pagatitle,
        'userinfo': userinfo
    }
    return render(request, 'super.html', context)
# <--------------------------------------------------------------------------- ('_') KITAP ('_') ------------------------------------------------------------------------>


def Kitap(request):
    cards = Card.objects.all().order_by('-id')
    pagatitle='Kitap'
    userinfo = ''
    if request.user.is_authenticated:
     userinfo = Userinfo.objects.get(user=request.user.id)
    
    query = request.GET.get('q')
    if query:
        cards = Card.objects.filter(Q(title__icontains=query) | Q(text__icontains=query)).distinct()

    context = {
        'cards': cards,
        'pagatitle': pagatitle,
        'userinfo': userinfo
    }
    return render(request, 'kitap.html', context)
# <--------------------------------------------------------------------------- ('_') DETAILS ('_') ------------------------------------------------------------------------>


def Detail(request,id):
    card = get_object_or_404(Card, id=id)
    cards = Card.objects.all().order_by('-id')
    userinfo = ''
    if request.user.is_authenticated:
     userinfo = Userinfo.objects.get(user=request.user.id)
    
    pagatitle=card.title
    query = request.GET.get('q')
    if query:
        cards = Card.objects.filter(Q(title__icontains=query) | Q(text__icontains=query)).distinct()
    
    if request.method == "POST":
        adet=int(request.POST['adet'])
        fiyat=card.price * adet
     
        if Shoping.objects.filter(card=card, user=request.user).exists():
                shoping = Shoping.objects.filter(user=request.user).get(card=card)
                shoping.adet += adet
                shoping.fiyat +=fiyat
                shoping.save()
        else:
            shoping=Shoping(user=request.user, card=card,adet=adet,fiyat=fiyat)
            shoping.save()
        
    context = {
        'card': card,
        'pagatitle': pagatitle,
        'cards': cards,
        'userinfo': userinfo,
    }
    return render(request, 'detail.html', context)


# <--------------------------------------------------------------------------- ('_') SHOPING ('_') ------------------------------------------------------------------------>

def Shopinguser(request):
    pagatitle = 'Sepetim'
    cards = Card.objects.all().order_by('-id')
    shops=Shoping.objects.filter(user=request.user)
    toplam = 0
    userinfo = ''
    
    query = request.GET.get('q')
    if query:
        cards = Card.objects.filter(Q(title__icontains=query) | Q(text__icontains=query)).distinct()
        
    if request.method == 'POST':
        adet=int(request.POST['adet'])
        card_id=request.POST['card-id']
        card=shops.get(id=card_id)
        card.adet=adet
        card.fiyat=adet * card.card.price
        card.save()
        return redirect('Shoping')
    
    for i in shops:
        toplam += i.fiyat

    if request.user.is_authenticated:
     userinfo = Userinfo.objects.get(user=request.user.id)    
    context = {
        'pagatitle': pagatitle,
        'shops': shops,
        'userinfo': userinfo,
        'toplam':toplam,
        'cards': cards,
    }

    return render(request, 'shoping.html', context)

# <--------------------------------------------------------------------------- ('_') DELTESHOP ('_') ------------------------------------------------------------------------>


def deleteShoping(request, id):
    shops = get_object_or_404(Shoping, id=id)
    shops.delete()
    return redirect('Shoping')


# <--------------------------------------------------------------------------- ('_') MYPRODUCTS ('_') ------------------------------------------------------------------------>
def myProducts(request):
    products = Card.objects.filter(user=request.user.id).order_by('-id')
    pagatitle = 'Ürünlerim'
    userinfo = ''
    if request.user.is_authenticated:
     userinfo = Userinfo.objects.get(user=request.user.id)
    
    context = {
        'products': products,
        'pagatitle': pagatitle,
        'userinfo': userinfo
    }
    return render(request, 'product/myproducts.html',context )

# <--------------------------------------------------------------------------- ('_') CREATE ('_') ------------------------------------------------------------------------>


def createProduct(request):
    pagatitle='Ürün Ekle'
    categorylist=Categori.objects.all()
    userinfo = ''
    if request.user.is_authenticated:
     userinfo = Userinfo.objects.get(user=request.user.id)
     
    context={
        'pagatitle': pagatitle,
        'categorylist': categorylist,
        'userinfo': userinfo,
    }
    if request.method == 'POST':
        title=request.POST['title']
        text=request.POST['text']
        price=request.POST['price']
        categoryid=request.POST['category']
        category=get_object_or_404(Categori,id=categoryid)
        image=request.FILES['image']
        
        card=Card(title=title,price=price,text=text,category=category,image=image,user=request.user)
        card.save()
        return redirect('myProducts')
  
    return render(request, 'product/create.html',context)
# <--------------------------------------------------------------------------- ('_') UPDATEPRODUCT ('_') ------------------------------------------------------------------------>


def updateProduct(request,id):
    categorylist=Categori.objects.all()
    pagatitle='Ürün Düzenle'
    product = get_object_or_404(Card, id=id)
    userinfo = ''
    if request.user.is_authenticated:
     userinfo = Userinfo.objects.get(user=request.user.id)
    context={
        'pagatitle': pagatitle,
        'categorylist': categorylist,
        'product': product,
        'userinfo': userinfo
    }
    
    
    if request.method == 'POST':
        title=request.POST['title']
        text=request.POST['text']
        price=request.POST['price']
        categoryid=request.POST['category']
        category=get_object_or_404(Categori,id=categoryid)
        try:
            image=request.FILES['image']
        except:
            image=product.image
        
        card=Card.objects.filter(id=id).update(title=title,price=price,text=text,category=category,image=image,user=request.user)
        
        return redirect('myProducts')
  
    return render(request, 'product/edit.html',context)


# <--------------------------------------------------------------------------- ('_') PRODELET ('_') ------------------------------------------------------------------------>
def deleteProduct(request,id):
    card=get_object_or_404(Card, id=id)
    card.delete()
    return redirect('myProducts')


# <--------------------------------------------------------------------------- ('_') R-USER ('_') ------------------------------------------------------------------------>
def registerUser(request):
    pagatitle = 'Register'
    context={
        'pagatitle': pagatitle,
    }
    if request.method=='POST':
        name=request.POST['name']
        sorname=request.POST['sorname']
        username=request.POST['username']
        email=request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
       
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                hataMessage = 'Bu kullanici adi kullanilmistir!'
                return render(request, 'users/register.html', {'hataMessage': hataMessage})
            
            elif User.objects.filter(email=email).exists():
                hataMessage = 'Bu email addresi  kullanilmistir!'
                return render(request, 'users/register.html', {'hataMessage': hataMessage})
            else:
                user = User.objects.create_user(first_name=name, last_name=sorname, email=email, username=username, password=password1)
                user.save()
                
                truMessage="Kaydiniz basariyla tammalnmisti ('_')"
                return render(request, 'users/login.html', {'truMessage': truMessage})
    return render(request,'users/register.html',context)
# <--------------------------------------------------------------------------- ('_') L-USER ('_') ------------------------------------------------------------------------>
truMessage=None
def loginUser(request):
    
    global truMessage
    if truMessage:
        return render(request, 'users/login.html', {'truMessage': truMessage})
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login (request,user)
            return redirect('index')
        else:
            hataMessage='kullanici adi veya Sifreniz yanlis!'
            return render(request, 'users/login.html', {'hataMessage': hataMessage})
        
    return render(request,'users/login.html')

# <--------------------------------------------------------------------------- ('_') LOGOUT ('_') ------------------------------------------------------------------------>
def logoutUser(request):
    logout(request)
    return redirect('index')

# <--------------------------------------------------------------------------- ('_') CHANGEPS ('_') ------------------------------------------------------------------------>
def changePassword(request):
    userinfo = Userinfo.objects.get(user=request.user.id)
    pagatitle = 'Şifre Değiştir'
    
    if request.method =='POST':
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1 == password2:
            user=User.objects.get(username=request.user)
            user.set_password(password1)
            user.save()
            logout(request)
            return redirect('loginUser')
        
    context={
        'pagatitle': pagatitle,
        'userinfo': userinfo,
    }
    return render(request,'users/change.html',context)