# döngüler - loops -start

# i=0
# i<10 == True

# iterate etmek, iteration

for i in range(0,10):
    print(i)

ogrenciler = ["Volkan","Süeda","Zühal","Selen","Ümit"]
#length
print(len(ogrenciler))
# 5
# 0, 1, 2, 3, 4

#break => ilgili döngünün o anda kırılmasını (bitirilmesini) sağlar

for i in range(len(ogrenciler)):
    if i==3:
        break
    print(f"{i+1}. Öğrenci: {ogrenciler[i]}")

#pass => ilgili alanın bodysini boş bırakabilmemize olanak sağlar
for i in range(0,10):
    pass

#continue => iterasyondaki current değeri atla, bir sonraki değer ile devam et
for i in ogrenciler:
    if i=="Volkan":
        continue
    print(f"Öğrenci: {i}")


# while booleanDeger
#infinite loop - sonsuz döngü
# ctrl+c => terminali durduran manual işlem
i = 0
while i < 10:
    i = i + 1
    if i==3:
        break
    print(f"While içerisindeki i değeri: {i}")
    

# döngüler - loops -end
