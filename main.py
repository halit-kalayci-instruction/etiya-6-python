print("Merhaba Etiya") 
print("Hoş geldiniz")

# yorum

# değişkenler -start
# metinsel, numerik, obje

# string
text = "Merhaba"

print(text)
print(text)
print(text)
text = "Selam"
print(text)
print(text)

studentCount = 45 # int, integer => tam sayı
print(studentCount + 5)

averagePoint = 25.5 
print(averagePoint + 5)

isVerified = True # bool, boolean => True veya False
print(isVerified)

print(type(text))
print(type(studentCount))
print(type(averagePoint))
print(type(isVerified))
# değişkenler -end

# operatörler -start
number = 10
# matematiksel operatörler 
print(10 + 10)
print(number + number)

print(number - 5)

print(number / 2)

print(number * 5)

# mod operatörü => sol tarafdaki değerin sağ taraftaki değere bölümünden kalan sonuç
print(number % 3)


print(number + ((10 - number) * (5 / 10)))

# mantıksal operatörler - karşılaştırma operatörleri
print(10 == 10) #true
print(11 == 10) #false

print(10 != 10) #false
print(11 != 10) #true

print(number > 10) #false
print(number >= 10) #true

print(number < 10) #false
print(number <= 10) #true

# operatörler -end

# diziler - listeler -start
print("**********************")
sayilar = [100, 200, 300, 400, 500, "Merhaba", 15.5, True] #listedeki tüm elemanların veri tipi aynı olmak zorunda DEĞİL!
#Programcı saymaya 0dan başlar
# index indis => 0 başlangıç değeri -1 son index
print(sayilar[0])
print(sayilar[5])

print(sayilar)
sayilar.append(100)
sayilar.append(600) # -> listenin sonuna eleman ekler.
print(sayilar)
sayilar.pop() # -> index'deki elemanı siler (default son index)
print(sayilar)
sayilar.remove("Merhaba") # -> pop'un aksine indexe göre değil değere göre siler.
print(sayilar)
sayilaraEkleme = [700,800,900]
sayilar.extend(sayilaraEkleme) #-> append'in aksine tek bir değer değil listedeki tüm elemanları listeye ekler
print(sayilar)
sayilar.clear() # -> Dizinin içini boşaltan fonksiyon
print(sayilar) 

# diziler - listeler -end
