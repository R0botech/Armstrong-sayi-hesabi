print("""			
    ========================
 	ARMSTRONG SAYI BELIRTME
	========================
    
    * Sayilari görmek icin 'i' yazın
    * Cikis yapmak icin 'q' yazın
""")

                                                 
while True:
    
    armstrong_d = input("_______sayi degerini girin_______:")                       
    basamak_degeri = str(armstrong_d)                                       

    basamak = len(basamak_degeri)                                              
    deger =list()                                                            
    deger.append(basamak)  

    if armstrong_d == 'i':
        print("Bazı armstrong sayıları: 153, 370, 371, 407")
    
    elif armstrong_d == 'q':
        print("Cikis yapiliyor...")
        break
            
    elif  deger == [3]: 
        armstrong_d =int(armstrong_d)                                                   
        deger1  = armstrong_d //100
        deger2  = (armstrong_d - deger1*100)//10
        deger3  = (armstrong_d - deger1*100 - deger2*10)
            
        hesaplama = (deger1**3) + (deger2**3) + (deger3**3)
            
        if hesaplama == armstrong_d:
                    
            print("girilen deger armstrong sayisidir")
                
        else:
            print("girilen deger armstrong sayisi degilir!")

    else:
        print("lutfen 3 veya 4 basamakli bir sayi giriniz!!")
