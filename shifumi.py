from random import randint
#base
a = ["pierre", "papier", "ciseaux" ]
#set play for computer
ordi = a[randint(0,2)]

game = False

while game == False:
    joueur =  input("pierre, papier, ciseaux?")

    if joueur == ordi:
        print("égalité")

    elif joueur == "pierre":
        if ordi == "papier":
            print("tas perdu")
        else:
            print("ta gagné")

    elif joueur == "papier":
        if ordi == "ciseaux":
          print("t'as perdu, contre un bot, sal merde")
        else:
            print("tu là fé, t'as batues 1 bot, bravaux!")

    elif joueur == "ciseaux":
        if ordi == "pierre":
            print("t'as perdu, contre un bot, sal mer2")
        else:
            print("tu l'a fait, ta batues 1 bot, bravo!")
    else:
        print("tu cés po écrir gros")



