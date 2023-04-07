#kulanıcıdan 10 adet sayı alalım ✅
#ve bu sayılar arasından en büyük 2. olanı kullanıcıya gösterelim

#döngüler-loops
#for loop
# i=0 , i = i + 1
# 0,1,2,3,4,5,6,7,8,9  < 10

biggestValue = 0 # 14,25
# 0 dan başlat, 10'dan küçük olana kadar döngüyü çalıştır, 
# döngü her çalıştığında i değerini 1 artır
for i in range(10):
    sayi = int(input(f"{i+1}. sayıyı giriniz: ")) #25
    if sayi > biggestValue:
        biggestValue = sayi

    
print(f"Girdiğiniz sayılar arasından en büyük olanı: {biggestValue}")


    

