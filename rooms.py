import random

hp = 100
tau = 0
nøkkel = 1
nøkkel_rom_2 = 0
nøkkel_rom_3 = 0
kniv = 0
potions = 3

def room1(): # definerer hva som skal skje i rom 1
    global hp
    hp -= 10
    print()
    print()
    print("Du tok skade,", hp, " liv igjen")
    print("du er nå i rom1, her skjer det et eller annet")
    print("Du må velge mellom 2 forskjellige dører")
    asking = True
    while asking == True:
        valg = input("A: rød dør B: blå dør -> ")
        if valg == "A" or valg == "B":
            asking = False
        else:
            print("Du skrev feil i input, velg et av alternativene")

    if valg == "A":
        room_2()  
    elif valg == "B":
        room_3()

def room_2():
    global nøkkel
    print("Du ser 2 dører, dør 1 er åpen, dør 2 er låst")
    valg = input("Gå i dør 1 eller låse opp dør 2 med nøkkelen du har?")

    if valg == "1":
        print("du gikk inn i dør 1")
        room_4()

    elif valg == "2" and nøkkel > 0:  # hvis mer enn 0 nøkler
        nøkkel -= 1
        print("Du låste opp dør 2")
        room_3()
    else:
        print("Du har ikke en nøkkel, så du gikk inn i dør 1 likevel")
        room_4()
    
   

def room_3():
    global hp
    print("Her møter du en bjørn.\n ")
    input()
    tilfeldig = random.randint(1,10)

    if tilfeldig <= 3: # mindre enn 3
        print("Bjørnen slo etter deg, du unngikk slaget\n")
    elif tilfeldig > 3: # mer enn 3
        print("Bjørnen slo deg, du tok skade.\n")
        skade = random.randint(10,20)
        hp -= skade # trekk ifra hp
        print(f"Du tok {skade} skade.")
        print(f"Du har {hp} hp igjen.\n")

def room_4():
    print("dette skjer i rom 4")
   


room_3()