import random

def main():
    pairs = matching()
    while pairs == {}:
        pairs = matching()

    for s in pairs:
        print (s + ":" + pairs[s])

def matching():
    sibs = ["Felicia", "Assunta", "Alfonse", "Salvatore", "Angelina"]
    mates = ["Donato", "Lucian", "Ashley", "Julie", "Grace"]
    getting_matched = sibs + mates
    available = sibs + mates
    pairs = {}
    for x in getting_matched:
        GMPlace = getPlace(x, sibs, mates)
        rand = random.choice(available)
        if len(available) == 1 and rand == x:
            return {}
        # identity check loop
        while rand == x:
            rand = random.choice(available)
        # get place of random choice from above
        MPPlace = getPlace(rand, sibs, mates)
        # if last two spaces are yourself and your mate
        if len(available) == 2:
            pot1 = getPlace(available[0], sibs, mates)
            pot2 = getPlace(available[1], sibs, mates)
            if pot1 == pot2:
                if GMPlace == pot1:
                    return {}
        # if last available space is your mate
        if len(available) == 1 and MPPlace == GMPlace:
            return {}
        # loop to ensure no placement matches
        while MPPlace == GMPlace:
            rand = random.choice(available)
            MPPlace = getPlace(rand, sibs, mates)
        available.remove(rand)
        pairs[x] = rand
    return pairs

def getPlace(x, sibs, mates):
        try: 
            place = sibs.index(x)
        except:
            place = mates.index(x)
        return place

if __name__ =="__main__":
    main()