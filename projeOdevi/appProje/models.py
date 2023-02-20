from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# <--------------------------------------------------------------------------- ('_') CATEC0RY ('_') ------------------------------------------------------------------------>

class Categori(models.Model):
    name = models.CharField(('Kategori adi'), max_length=50)

    def __str__(self):
        return self.name
    
    # <--------------------------------------------------------------------------- ('_') CARD ('_') ------------------------------------------------------------------------>
class Card(models.Model):
    user=models.ForeignKey(User, verbose_name=("Satici"), on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Categori, verbose_name=('Kategori'), on_delete=models.CASCADE, null=True)
    title = models.CharField(("Card Baslik"), max_length=100)
    text = models.TextField(("Card Yazisi"))
    image = models.FileField(("Card Resmi"), upload_to='', max_length=100, null=True)
    price = models.FloatField(('urun fiyati'), null=True)
    date_now = models.DateTimeField(("Paylasim Zamani"), auto_now_add=True)

    def __str__(self):
        return self.title
    
  # <--------------------------------------------------------------------------- ('_') SHOPING ('_') ------------------------------------------------------------------------>

class Shoping(models.Model):
      user=models.ForeignKey(User, verbose_name=("Kullanici"), on_delete=models.CASCADE)
      card=models.ForeignKey(Card, verbose_name=("Ürün"), on_delete=models.CASCADE )
      adet=models.IntegerField(("Adet"))
      fiyat=models.FloatField(("Toplam Fiyat"))
    
  # <--------------------------------------------------------------------------- ('_') USERIFO ('_') ------------------------------------------------------------------------>

class Userinfo(models.Model):
      user=models.ForeignKey(User, verbose_name=("Kullanici"), on_delete=models.CASCADE)
      image=models.FileField(("Imag"), upload_to=None, max_length=100)
      adress=models.CharField(("Adress"), max_length=150)
    