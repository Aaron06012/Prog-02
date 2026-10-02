kluisjes = open("Kluisjes.txt")


def aantal_kluizen_vrij() :

    regels = kluisjes.readlines()
    x = len(regels)
    resultaat = 12 - x

    return int(resultaat)

def nieuwe_kluis()



print(aantal_kluizen_vrij())




