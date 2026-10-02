
kluisjes = open("Kluisjes.txt")
regels = kluisjes.readlines()
def kluisnummer() :
    actueel = []

    for regel in regels:
        actueel.append(regel[0])
    return actueel

def kluiscode() :
    actueel = []

    for regel in regels:
        actueel.append(regel[0])
    return actueel

def nieuwe_kluis() :
    regelen = kluisnummer()
    antwoord = input("voor een geldige nummer in")

    if antwoord in regelen :
        print('dit nummer is niet beschikbaar')
    else :
        code = input("voor een geldige code in")
        if len(code) < 4 or ';' in code :
            print("te kort van een code")
        else :
         print("de code is correct")
         resultaat =antwoord+";"+code
         return resultaat








print (nieuwe_kluis())




#if antwoord not in regelen :
        #print('dit nummer is beschikbaar')



##

#def kluis_openen() :

#def kluis_teruggeven() :

#filehandle.close