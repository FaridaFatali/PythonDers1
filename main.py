print("Kodlamaio")

#String => metinsel ifade
baslik = "Taşıt Kredisi"
print(baslik)

baslik = "İhtiyaç Kredisi"
print(baslik)

# Yeni bir şey eklemediğimiz zaman en sondakını kullanıyor sanırım
print(baslik)

# int, integer => tam sayı
vade = 36
ekVade = 6
vade2 = "36"

# float, decimal, double
aylikOdeme = 200.50

# bool, boolean => True veya False
yukselisteMi = False

# matematiksel operatörler
# +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

# -
print(5 - 5)
print(vade - 12)
print(vade - ekVade)
print(36 - 6)

# *
print(5 * 5)
print(vade * 2)
print(vade * ekVade)
print(10 * 10)

# /
print(5 / 5)
print(vade / 2)
print(vade / ekVade)
print(10 / 2)
# Değerin tam değil float olarak dönmesinin sebebi şu ki, diğer operatörler kullandığımız zaman eğer tam sayı yazdıysak, sonuç da tam olacaktır, 
# ama bölme işlemi zamanı tam sayı kullandığımız zaman bile sonucu tam almayabiliriz, mesela, 9/2, bu yüzden her zaman bölme işlemlerinde sonuç float olarak verilir.

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20
print(yeniVade)
print(indirimliFiyat)

# % => mod operatör
print(10 % 2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)

# mantıksal operatörler
print(1 == 1)
print(1 == 2)

# bir kaç satrı yorum satrı haline getirmek için hepsini işaretleyip ya #CTRL K + CTRL C tuşlarını kullana yada 
# sadece CTRL ve / tuşlarını aynı anda kullanarak yapabiliriz
print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

print(1 != 1)
print(1 != 2)

# or and

# or (veya) olduğu zaman ikisinden birinin true olması yeterli. 
# 1. kısım true olduğunda 2. kısma bakmadan True oluyor. 1. kısım false olduğu zaman, 2. kısma bakıyor, 
# o true ise True oluyor, false ise sonuç False oluyor.

# and (ve) durumunda ise her ikisinin true olması gerekir,
# 1. kısma bakıyor, o true ise 2. kısma geçiyor, o da true ise sonuç True oluyor.
# 1. kısım false olursa, 2. kısma bakmaya gerek duymadan False oluyor.


# or => veya
# and => ve
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 and 3 > 2)

print(2 > 1 or 1 > 2 and 3 > 2)


# karar yapıları
# if else
sayi1 = 15
sayi2 = 15
# sayi1 sayi2'den büyükse ekrana sayi 1 daha büyük yazdır
# condition

# indent
if sayi1 <= sayi2:
    print("Sayi 1 Sayi 2'den küçüktür")
elif sayi1 == sayi2:
    print("İki sayı eşittir")
# eğer if ve else if bloklarından hiç birine girmezse
else:
    print("Sayi 1 Sayi 2'den büyüktür")

print("**********")

if sayi1 <= sayi2:
    print("Sayi 1 Sayi 2'den küçüktür")

if sayi1 == sayi2:
    print("İki sayı eşittir")
else:
    print("Sayi 1 Sayi 2'den büyüktür")

print("Burası if bloğunun dışıdır")

