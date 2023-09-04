def room1(): # definerer hva som skal skje i rom 1
    print("du er nå i rom1, her skjer det et eller annet")
    print("Du må velge mellom 2 forskjellige dører")
    valg = input("A: rød dør B: blå dør -> ")

    if valg == "A":
        room2()  
    if valg == "B":
        room3()

def room2():
    print("dette er i rom 2")
    room1()

def room3():
    print("dette skjer i rom 3")
    room1()


room1()