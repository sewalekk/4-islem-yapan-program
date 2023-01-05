# 4 işlem yapan hesap makinesi

sayi1=int (input("Sayı 1: "))
sayi2=int (input("Sayı 2: "))
print("Toplama=1, Çıkarma=2, Çarpma=3, Bölme=4")
islem=int(input("Hangi işlemi yapmak istersiniz? "))

if(islem==1):
    sonuc=sayi1+sayi2
elif(islem==2):
    sonuc=sayi1-sayi2
elif(islem==3):
    sonuc=sayi1*sayi2
elif(islem==4):
    sonuc=sayi1/sayi2

print("İşlem Sonucu: {}".format(sonuc))