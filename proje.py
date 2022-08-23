import random

secenek = ["taş", "kağıt", "makas"]

print("Oyuna hoşgeldiniz oyundan çıkmak için q basınız.")

while True:
    secim=input("Taşmı kağıtmı makasmı ?").lower()
    bil_secim= random.choice(secenek)

    if secim == "q":
        print("oyundan başarıyla çıkış yaptınız")
        break

    elif(secim == bil_secim):
        print("Berabere")
    
    elif(secim == "taş" and bil_secim=="kağıt"):
        print("Bilgisayar Kazandı")
    
    elif(secim == "makas" and bil_secim=="taş"):
        print("Bilgisayar Kazandı")
    
    elif(secim == "kağıt" and bil_secim=="makas"):
        print("Bilgisayar Kazandı")

    else:
        print("Kazandınız")
