from random import randint
#base
a = ["pierre", "papier", "ciseaux" ]
#set play for computer
ordi = a[randint(0,2)]

game = False

while game == False:
    joueur =  input("pierre, papier, ciseaux?")



    if joueur == ordi:
        print("tie the computer did", ordi)
        ordi = a[randint(0,2)]
    elif joueur == "X-ray":
            print(ordi)

    elif joueur == "pierre":
        if ordi == "papier":
            print("you lost ):, the computer did", ordi)
            ordi = a[randint(0,2)]
        else:
            print("you won! the computer did", ordi)
            ordi = a[randint(0,2)]


    elif joueur == "papier":
        if ordi == "ciseaux":
          print("you lost ): the computer did", ordi)
          ordi = a[randint(0,2)]
        else:
            print("you won! the computer did", ordi)
            ordi = a[randint(0,2)]


    elif joueur == "ciseaux":
        if ordi == "pierre":
            print("you lost ): the computer did", ordi)
            ordi = a[randint(0,2)]
        else:
            print("you won! the computer did", ordi)
            ordi = a[randint(0,2)]

    else:
        print("incorect imput")
