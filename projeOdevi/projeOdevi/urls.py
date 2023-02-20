"""projeOdevi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appProje.views import *
# SQL veri tabaninda gelen resim dosyalari icin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('elektronik/',Elektronik,name='Elektronik'),
    path('Ev/',Ev,name='Ev'),
    path('anne/',Anne,name='Anne'),
    path('spor/',Spor,name='Spor'),
    path('kozmetik/',Kozmetik,name='Kozmetik'),
    path('super/',Super,name='Super'),
    path('kitap/',Kitap,name='Kitap'),
    path('detay/<id>/',Detail,name='Detail'),
    # <--------------------------------------------------------------------------- ('_') MYPRODUCTS('_')----------------------------------------------------------------------->
    path('products/', myProducts, name='myProducts'),# Ürünlerim
    path('createproduct/', createProduct, name='createProduct'),  # Ürün ekleme
    path('deleteproduct/<id>/', deleteProduct, name='deleteProduct'), # Ürün silme
   
    path('updateproduct/<id>/', updateProduct,name='updateProduct'),  # Ürün Düzünleme
    
    # <--------------------------------------------------------------------------- ('_') SHOPING('_')----------------------------------------------------------------------->
    path('shoping/', Shopinguser, name='Shoping'),  # Sepetim
    path('deleteShoping/<id>/', deleteShoping,name='deleteShoping'),  # Ürün silme
    
    
    # <--------------------------------------------------------------------------- ('_') USERS ('_')----------------------------------------------------------------------->
    path('login/',loginUser,name='loginUser'), #giris
    path('register/',registerUser,name='registerUser'), #kaydol
    path('logout/',logoutUser,name='logoutUser'), #cikis
    path('changepassword/', changePassword, name='changePassword'), #sifre degistir

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
