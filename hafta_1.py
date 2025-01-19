"""
#string işlemleri
isim='basak'
print(isim[2]) #ifadenin 3.harfini yazdırır
print(isim[0:3]) #baştan itibaren ilk 3 harfi yazdırır 3 dahil değil
print(isim[-0:-3]) #sondan itibaren son 3 harfi yazdırır 3 dahil değil
print(len(isim)) #stringin uzunluğunu verir
print(isim.title()) #stringin ilk harfini büyütür
print(isim.upper()) #stringin tüm harflerini büyütür
print(isim.lower()) #stringin tüm harflerini küçültür
print(isim.find('e')) #stringimizin içinde istenilen texti arar  

#koşul ifadeleri
rainy=True
sunny=True

if rainy:
    print("wear a jacket")

elif sunny:
    print("wear a sunglasses")

else:
    print("do nothing")


#List (ordered and changable) []bu şekilde ifade edilir
fruits=["apple","orange","banana","coconut"]
print(fruits[0])

for fruit in fruits:
    print(fruit)

fruits.append("pineapple")#listeye ekleme komutu
fruits.remove("apple")#listeden silme komutu
fruits.insert(0,"pineapplee")#eklemeyi istediğimiz yere yapar
fruits.sort()#sıralar
fruits.reverse()#elemanların yerini tersine çeviri

#Set (unordered and immutable) değiştirilemez ama ekleme ve çıkarma yapılabilir
#{}bu şekilde ifade edilir
fruits={"apple","orange","banana","coconut"}
fruits.add("pineapple")#ekleme komutu
fruits.remove("apple")# silme komutu
fruits.pop()#eleman siler ve geri döndürür

#tuple (ordere and unchangeable) ()bu şekilde ifade edilir
#listten daha hızlı olduğu için bu durumlarda kullanılır
fruits=("apple","orange","banana","coconut")
fruits.index("apple")#indexini verir
fruits.count("coconut")#adet sayısını verir 

#Exception Handling
try:
    x=int(input("ilk sayıyı giriniz:"))
    y=int(input("ilk sayıyı giriniz:"))
    
    print(x/y)
except(ZeroDivisionError,ValueError):
   print("hata var") 

#Dosya işlemleri
with open ("deneme.txt","r") as f #dosyayı aç ve f olarak tanımlar
icerik=f.read()
print(icerik)

icerik=f.readlines() #satır satır okumayı sağlar
print(icerik)
for satir in icerik:
    print(satir,end="")#arada boşluk bırakmadan satır satır yazdırır


pozisyon=f.tell() #imlecin hangi satırda olduğunu gösterir
f.seek(0) #dosyanın 0. karakterine gider

#istediğimiz miktarda olan dosyayı okumak için :
okunacak_miktar=10
icerik=f.read(okunacak_miktar)
while len(icerik)>0:
    print(icerik,end=" ")

with open("deneme2.txt","w") as f: #yazma moduyla açar
    f.write("Python") #içerik yazdırır

with open("deneme.txt") as okunacak:
    with open("deneme2.txt") as yazilacak:
        for satir in okunacak:
            yazilacak.write(satir) #text1 in içeriğini text2 ye geçirir
       


"""

import random
import string

def sifre_olustur(uzunluk):
    if uzunluk < 4:
        return "Şifre uzunluğu en az 8 olmalıdır."

    # Şifre için karakterleri atadık
    kucuk_harfler = string.ascii_lowercase
    buyuk_harfler = string.ascii_uppercase
    rakamlar = string.digits
    ozel_karakterler = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    # Şifre için her türden en az bir karakter seçtik
    sifre = [
        random.choice(kucuk_harfler),
        random.choice(buyuk_harfler),
        random.choice(rakamlar),
        random.choice(ozel_karakterler)
    ]

    # Kalan karakterleri rastgele seçtik
    tum_karakterler = kucuk_harfler + buyuk_harfler + rakamlar + ozel_karakterler
    sifre += random.choices(tum_karakterler, k=uzunluk - 4)

    # Şifreyi karıştırdık
    random.shuffle(sifre)

    return ''.join(sifre)

# Kullanıcıdan şifre uzunluğu aldık ve sonucu yazdırdık
try:
    uzunluk = int(input("Şifre uzunluğunu girin: "))
    print("Oluşturulan şifre:", sifre_olustur(uzunluk))
except ValueError:
    print("Lütfen geçerli bir sayı girin.")
