


def vizehesapla():
    print('*' * 47)
    vize =  int(input("VİZE NOTUNUZ :"))
    final = int(input("FİNAL NOTUNUZ :"))
    print('*' * 47)


    ortalama = vize*0.4 + final*0.6
    print("ORTALAMA :",ortalama)

    if ortalama < 50:
        print("KALDINIZ!!!")
        print(50-ortalama , "PUAN GEREKLİ")
        print(50-ortalama , "PUAN ALMAK İÇİNDE FİNALDEN EN AZ" , (50-vize*0.4)/0.6 , "PUAN ALMANIZ GEREKİYORDU")
    else:
        print("GEÇTİNİZ")
    input("---DEVAM ETMEK İÇİN ENTER---")

def finalkacalmamlazim():
    vize = int(input("VİZE :"))
    finalalma = (50-vize*0.4)/0.6
    print("EN AZ" , finalalma , "ALMAN GEREKİYOR!")


while True:
 print('*'*47)
 print("---ÜNİVERSİTE PUAN HESAPLAYICIYA HOŞGELDİNİZ---")
 print("1-VİZE FİNAL HESAPLA")
 print("2-FİNALDEN KAÇ ALMAM GEREKİYOR?")
 print('*' * 47)
 secim = input('SEÇİMİNİZ :')


 if secim=='1':
     vizehesapla()
 elif secim=='2':
     finalkacalmamlazim()