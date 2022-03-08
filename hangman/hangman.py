import random
PROBALKOZASOK_MAX = 10
SZOFILE = open('szavak.txt', mode='r', encoding='utf-8')
KITALALANDO = random.choice([x.strip() for x in SZOFILE.readlines() if len(x.strip()) >= 4])
KITALALANDO_C = "".join(["*" for x in KITALALANDO])
PROBALKOZASOK = []

def is_char(s: str):
    if len(s) == 1:
        return True
    return False

while PROBALKOZASOK_MAX != 0:
    print("A szó eddig: {}, eddigi találataid: [{}].".format(KITALALANDO_C, ", ".join(PROBALKOZASOK)))
    print("Ennyi találatod maradt: {}".format(PROBALKOZASOK_MAX))
    talalat = input("Írj be egy karaktert, ami szerinted a szóban benne van!\n> ").upper()

    if not is_char(talalat):
        print("Ez nem egy karakter!")
        continue
    

    PROBALKOZASOK.append(talalat)
    KITALALANDO_C = "".join(["*" if x not in PROBALKOZASOK else x for x in KITALALANDO])

    if KITALALANDO_C == KITALALANDO:
        for x in range(10):
            print("Kitaláltad a szót, gratula! B)")
        break

    if talalat not in KITALALANDO:
        PROBALKOZASOK_MAX -= 1
    
        if PROBALKOZASOK_MAX == 0:
            print("Nem tudtad kitalálni a szót :(")
            print('ez volt a szo amugy:', KITALALANDO)
            break
input("Nyomja meg az ENTER-t a kiklépéshez.\n")