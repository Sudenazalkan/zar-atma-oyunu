# zar atma oyunu
import random

toplam_b = 0
toplam = 0
while True:
    zar1 = int(input("Lütfen 1 ile 6 arasında bir sayı giriniz: "))

    if zar1 > 6:
        print("Girdiğiniz değer 1-6 aralığında olmalı.")
        break
    if zar1 == 1:
        x = random.randint(1, 6)
        print("Bilgisayarın attığı zar değeri:{}".format(x))

        toplam_b = toplam_b + x
        print("Bilgisayarın puanı:{}".format(toplam_b))

        toplam = toplam + zar1
        print("Puanınız:{}".format(toplam))

    if zar1 > 1:
        a = int(input("Devam etmek için 1'e turu sonlandırmak için 2'ye basınız: "))
        if a == 1:
            zar2 = int(input("Lütfen 1 ile 6 arasında bir sayı giriniz: "))
            if zar2 > 1:
                x = random.randint(1, 6)
                print("Bilgisayarın attığı zar değeri:{}".format(x))
                toplam_b = toplam_b + x
                print("Bilgisayarın Puanı:{}".format(toplam_b))
                toplam = zar1 + zar2 + toplam
                print("Puanınız:{} ".format(toplam))
            if zar2 == 1:
                print("Maalesef bu turdan puan alamadınız :(")
                x = random.randint(1, 6)
                print("Bilgisayarın attığı zarın değeri:{}".format(x))
                toplam_b = toplam_b + x
                print("Bilgisayarın puanı:{}".format(toplam_b))
                print("Puanınız:{}".format(toplam))

        if a == 2:
            x = random.randint(1, 6)
            print("Bilgisayarın attığı zar değeri:{}".format(x))
            toplam_b = toplam_b + x
            print("Bilgisayarın Puanı:{}".format(toplam_b))
            toplam = toplam + zar1
            print("Puanınız:{} ".format(toplam))

    if toplam >= 100:
        print("Tebrikler Kazandınız :)")
    if toplam >= 100:
        break
    if toplam_b >= 100:
        print("Bilgisayar kazandı")
        break