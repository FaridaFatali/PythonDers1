# Veri tipleri:
# String tip => Metinsel ifade için kullanılır. Bir değişkeni metinsel ifadeyle verdiğimiz zaman çift tırnak içinde yazarız:
metinselTip = "Buraya istediğimiz kadar kelime veya cümle yazabiliriz"

# Numeric (Sayısal) tipler => Sayılarla gerçekleşen işlemler için farklı numeric tipler kullanırız.
# Mesela, tam sayı için int, integer  kullanıyoruz:
tamSayi = 15

# Tam olmayan yani ondalıklı sayılar için ise float, decimal, double kullanıyoruz
ondalikliSayi = 35.6

# Mantıksal tip => Mantıksal sorgular için Boolean, Bool tipi kullanıyoruz. Yani almak istediğimiz sonucun doğru (true) veya yanlış (false) olduğunu bu veri tipiyle anlıyoruz:
# True ve False burada büyük harflerle başlıyor
avrupaMi = True
asyaMi = False

# Dizi tipleri => Eğer birden fazla şeyi bir arada tutmak istiyorsak, o zaman dizi tipleri - list, tuple, range kullanıyoruz:
teknolojiler = ["bilgisayar", "telefon", "tablet"]

# Adresleme tipleri => Özellikle bir nesneye ait bilgileri burada dict tipi olarak tutabiliriz:
adreslemeTipi = {"isim" : "kodlama.io", "alan" : "Programlama/Yazılım", "ogrenci" : 5000}

# Küme tipleri => Bir şeyleri küme halinde tutmak için set veya frozenset tipleri kullanıyoruz:
telefonlar = {"Samsung", "iPhone", "Redmi", "Xiaomi"}

# Binary tipler => bytes, bytearray, memoryview tipleri var
binaryTipi = b"Hello"
# veya binaryTipi = bytearray(5)


# ---------------------------------------


# Kodlama.io sitesinde değişken olarak kullanılan veriler ve veri tipleri
# Dizi tipleri
kurslar = ["JavaScript", "Python & Selenium", "Java", "C# and Angular", "Java and React", ".NET", "Temel Kurs"]
ogretmenler = ["Engin Demiroğ", "Halit Enes Kalaycı"]

# Metinsel tipler
kurs1 = "Yazılım Geliştirici Yetiştirme Kampı (JavaScript)"
kurs2 = "Senior Yazılım Geliştirme Kampı (.NET)"
kursIcerigi = "Ders Programı"
# ve s.

# Sayısal tipler int, float
kursTarihi = 2023
dersSayisi = 6
kursSuresi = 2
kursSuresi2 = 1.5

# Karar yapılarını profilimize girerken kullanabiliriz:

myGmail = "farida@gmail.com"
myPassword = "111111"

requestGmail = myGmail
requestPassword = myPassword

if requestGmail == myGmail and requestPassword == myPassword:
    print("Giriş başarıyla tamamlandı")
else:
    print("Kullanıcı adı veya şifre yanlış")

# Benim bulabildiklerim bunlar, umarım doğru yazmışımdır.


