# -------------------------------------------------------------------------Not Ortalması Hesaplama(Çanlı)--------------------------------------------------
Vize=float(input("Vize Notunuzu Giriniz: "))
Final=float(input("Final Ortalamanızı giriniz: "))
SınıfOrt=float(input("Sınıf Ortalamasını giriniz:  Eğer sınf ortalaması 60 dan aşşağıda ise çan açılacaktır"))
öğrenciO= (Vize*0.4) + (Final*0.6) 
if Final<40:
    print("Finaliniz minimum 40 olmalıdır sınavdan kaldınız")
    
else:

 if SınıfOrt<60:
    print("Sınıf ortalaması 60 dan düşüktür çan açılmıştır")
    if SınıfOrt<öğrenciO:
        print(f"Tebrikler Sınavı Geçtiniz Sınıf ortalaması: {SınıfOrt} sizin ortalamanız: {öğrenciO}")
    else:
        print(f"Ortalamanız sınıf ortalamasının altında kaldığı için dersten kaldınız sizin ortalamanız: {öğrenciO} sınıf ortalaması {SınıfOrt} ")   
 else:
    if 60<=öğrenciO:
        print(f"Tebrikler dersten geçtiniz ortalamnız: {öğrenciO}")
    else:
        print(f"Maalesef dersten kaldınız ortalamanız: {öğrenciO}")

# ------------------------------------------------------------Vücut Kitle Endeksi hesaplama------------------------------------------------------------------------------------------

# kulKg=float(input("Lütfen Kg cinsinden kilonuzu giriniz"))
# kulBoy=float(input("Lütfen 'm' cinsinden boyunuzu giriniz"))
# vucutKitleEndeksi=kulKg / (kulBoy * kulBoy)

# if vucutKitleEndeksi<=18.5:
#     print("Fazla zayıfsınız")
# elif 18.5<vucutKitleEndeksi<24.9:
#     print("Normal Kilodasınız")
# elif 25<vucutKitleEndeksi<29.9:
#     print("Fazla Kilolusunuz")
# elif 30<vucutKitleEndeksi<34.9:
#     print("1.Sınıf obez sınıfındasınız")
# elif 35<vucutKitleEndeksi<39.9:
#     print("2. Sınıf obez sınıfındasınız")
# else:
#     print("3. Sınıf obez sınıfındasınız")

# Tek çift sayı kontrol
# sayi=int(input("Bir sayı giriniz"))

# if sayi % 2 == 0:
#     print("Sayı çifttir")
# else:
#     print("Sayı tektir")

# Hesap Makinası

# x=int(input("Birinci sayınızı giriniz"))
# y=int(input("İkinci sayınızı giriniz"))
# islem = input("Yapmak istediğiniz işlem (+, -, *, /): ")

# if islem =="+":
#     print(x+y)
# elif islem =="-":
#     print(x-y)
# elif islem =="*":
#     print(x*y)
# elif islem =="/":
#     if y ==0:
#         print("0 a bölme yapılamaz")
#     else:
#         print(x/y)
# else:
#     print("Geçersiz işlem girildi")

# Şifre Doğrulama

# denemeSayisi=0
# kullanicilar={
#     "Serkan":"1234",
#     "Naz":"Prenses",
#     "Suko":"GAY"

# }
# nickName=input("Kullanıcı adınızı giriniz")
# password=input("Şifre giriniz")

# if nickName in kullanicilar:
#     if password == kullanicilar[nickName]:
#         print("Sisteme girdiniz")
#     else:
#         print("Yanlış şifre girdiniz")
# else:
#     print("Yanlış kullanıcı adı")

# Çarpım Tablosu

# number=int(input("Çarpım tablosunu almak istedğiniz sayıyı girin"))

# for x in range(1,11):
#     print(f"{x} x {number} ={x*number}")


# Faktöriyel hesaplama
# fak=int(input("Faktöriyelini istedğiniz sayıyı giriniz"))
# sonuc=1

# for x in range(1,fak+1):
#     sonuc=sonuc*x
# print(sonuc)    

# Asal sayı kontrol

# sayi=int(input("Asal sayı olup olmadığını kontol etmek istediğinz sayıyı giriniz"))
# asal=True

# for x in range(2,sayi):
#     if sayi % x == 0:
#         asal=False
#         break
# if asal:
#         print("Sayı asaldır")
# else:
#         print("Asal değildir")


# Belirli aralıktaki asal sayılar

# asalBaslangıc=int(input("Asal için başlangıç sayınızı alın"))
# asalBitis=int(input("Bitiş sayısını giriniz"))

# for x in range(asalBaslangıc,asalBitis):
#     asal=True
#     for i in range(2,x):
#         if x % i == 0:
#             asal=False
#             break
#     if asal:
#      print(x)

#  Rastgele sayı üretici
# import random
# minSayi=1
# maxSayi=100
# randomNumber=random.randint(minSayi,maxSayi)

# print(randomNumber)
