ime = str(input("Unesite ime:"))

def funkcija(ime):
    pozdrav = print("Pozdrav "+ ime +"!")
    return pozdrav
funkcija1 = lambda ime: print("Dobrodošao " + ime + "!")
def funkcija2(funkcija):
    funkcija(ime)
funkcija2(funkcija)
funkcija2(funkcija1)
