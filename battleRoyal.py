import random , os

class Düsman():
    def __init__(self):
        self.sagmi = True
        self.saglik = random.randint(40, 80)
        self.kalkan = random.randint(50,80)
        self.güc = random.randint(60,80)

    def vur(self,Player):                       #Vurma olayını gerçekleştirme
        damage = self.güc - Player.kalkan
        Player.saglik -= damage 
        if Player.saglik <= 0 :
            Player.sagmi = False

class Player():
    def __init__(self):
        self.sagmi = True
        self.saglik = 450
        self.kalkan = 150
        self.güc = 100

    def vur(self,Düsman):               #Vurma olayını gerçekleştirme
        damage = self.güc - Düsman.kalkan
        Düsman.saglik -= damage
        if  Düsman.saglik <= 0 :
            Düsman.sagmi = False
            düşmanlar.remove(Düsman)

düşmanlar = list()

for i in range(10):    #düşamlarımızı ekliyor
    düşmanlar.append(Düsman())


player = Player()

while True:
    os.system("clear")  # windows için cls              # ekranı temizleyecek
    print(" player durumu --->>> Sağlık : {} -------- Kalkan : {} --------- Güç : {} " .format(player.saglik,player.kalkan,player.güc))

    if player.sagmi == False:
        print("Game Over")
        quit()

    if not düşmanlar:
        print("Tebriklerrrr")
        quit()

    for i in düşmanlar:
        print("{}. Düşman --->>> Sağlık  : {} ------ Kalkan : {} --------- Güç : {} " .format(düşmanlar.index(i), i.saglik,i.kalkan, i.güc))
    


    sec = int(input("""HAYDİ  
                    DİŞİNE GÖRE 
                BİR DÜŞMAN SEÇ !!!!"""))
    
    
    Düsman = düşmanlar[sec]
    player.vur(Düsman) 

    saldıran =düşmanlar[random.randint(0 , len(düşmanlar)-1)]
    saldıran.vur(Düsman)


 




