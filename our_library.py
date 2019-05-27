import numpy as np
import matplotlib.pyplot as plt

''' Narejeno dne 17.05.2019 by Rok Špan, Juš Kolarič'''

def Meshgrid_DMX(pan2=0,pan1=0,pan4=0,pan3=0, tilt2=0,tilt1=0,tilt4=0,tilt3=0, tocke = 5):
    '''Funkcija sprejme koordinate luči "pan" in "tilt", ki jih dobimo z klikanjem ogljišč v GUI-u
    
    - argument_1: število točk v vrstici mreže, po kateri se bo luč zapeljala za kalibracijo
    - argument_2,3: pan, tilt
    '''
    # Ustvarimo število točk za MREŽO po kateri se bo peljala luč za kalibracijo
    stevilo_tock_v_vrstici = tocke
    stevilo_tock = stevilo_tock_v_vrstici**2
    slika = np.zeros((stevilo_tock,2))
    luc_na_sliki = np.zeros((stevilo_tock,2))
    DMX = np.zeros((stevilo_tock,2))
    DMX_calib = np.zeros((stevilo_tock,2))
    # Koordinate točk, ki še niso preračunane dobijo vrednost "nan"
    DMX[DMX == 0] = np.nan
    # Pozicije skrajnih točk - za vrstni red v matriki
    poz_1 = 0
    poz_2 = int(stevilo_tock_v_vrstici-1)
    poz_3 = int(stevilo_tock-stevilo_tock_v_vrstici)
    poz_4 = stevilo_tock-1
    # Določanje skrajnih točk (ogljisca odra)
#     pan1 = 5 # Povezi z GUI
#     tilt1 = 0 # povezi z GUI
#     pan2 = 5 # Povezi z GUI
#     tilt2 = 0 # povezi z GUI
#     pan3 = 5 # Povezi z GUI
#     tilt3 = 0 # povezi z GUI
#     pan4 = 5 # Povezi z GUI
#     tilt4 = 0 # povezi z GUI
    
    DMX[poz_1] = pan1, tilt1
    DMX[poz_2] = pan2, tilt2
    DMX[poz_3] = pan3, tilt3
    DMX[poz_4] = pan4, tilt4

    # koordinate v skrajnih točkah - uporaba za enačbe ipd.
    poz_1_x = DMX[poz_1][0]
    poz_1_y = DMX[poz_1][1]
    poz_2_x = DMX[poz_2][0]
    poz_2_y = DMX[poz_2][1]
    poz_3_x = DMX[poz_3][0]
    poz_3_y = DMX[poz_3][1]
    poz_4_x = DMX[poz_4][0]
    poz_4_y = DMX[poz_4][1]

    # enačbe za MREŽO (izračun koordinat točk med ogljisci oz. pozicijami)

    # poz3        poz4
    #     |------|
    #     |      |
    #     |      |
    #     |------|
    # poz1        poz2

    grid_poz_1_2_x = abs(poz_2_x-poz_1_x)/(stevilo_tock_v_vrstici-1)
    grid_poz_1_2_y = abs(poz_2_y-poz_1_y)/(stevilo_tock_v_vrstici-1)

    grid_poz_3_4_x = abs(poz_4_x-poz_3_x)/(stevilo_tock_v_vrstici-1)
    grid_poz_3_4_y = abs(poz_4_y-poz_3_y)/(stevilo_tock_v_vrstici-1)

    grid_poz_1_3_x = abs(poz_3_x-poz_1_x)/(stevilo_tock_v_vrstici-1)
    grid_poz_1_3_y = abs(poz_3_y-poz_1_y)/(stevilo_tock_v_vrstici-1)

    grid_poz_2_4_x = abs(poz_2_x-poz_4_x)/(stevilo_tock_v_vrstici-1)
    grid_poz_2_4_y = abs(poz_2_y-poz_4_y)/(stevilo_tock_v_vrstici-1)

    # Preracun in zapis koordinat skrajnih točk mreže
    # DMX[pozicija v mrezi][koordinata x,y]

    for i in range(int(stevilo_tock_v_vrstici)-2):
        # poz 1-2
        if poz_1_x < poz_2_x:
            DMX[i+1][0] = grid_poz_1_2_x*(i+1) + min(poz_2_x,poz_1_x)
        else:
            DMX[i+1][0] = abs(grid_poz_1_2_x*(i+1) - max(poz_2_x,poz_1_x))
        if poz_2_y > poz_1_y: # SPREMENI ČE ZAFRKAVA
            DMX[i+1][1] = grid_poz_1_2_y*(i+1) + min(poz_2_y,poz_1_y)
        else:
            DMX[i+1][1] = abs(grid_poz_1_2_y*(i+1) - max(poz_2_y,poz_1_y))

        # poz 3-4
        if poz_3_x < poz_4_x:  # SPREMENIL
            DMX[(i+1)+(stevilo_tock-stevilo_tock_v_vrstici)][0] = grid_poz_3_4_x*(i+1) + min(poz_3_x,poz_4_x)
        else:
            DMX[(i+1)+(stevilo_tock-stevilo_tock_v_vrstici)][0] = abs(grid_poz_3_4_x*(i+1) - max(poz_3_x,poz_4_x))
        if poz_3_y < poz_4_y:
            DMX[(i+1)+(stevilo_tock-stevilo_tock_v_vrstici)][1] = grid_poz_3_4_y*(i+1) + min(poz_3_y,poz_4_y)
        else:
            DMX[(i+1)+(stevilo_tock-stevilo_tock_v_vrstici)][1] = abs(grid_poz_3_4_y*(i+1) - max(poz_3_y,poz_4_y))

        # poz 1-3
        if poz_3_x > poz_1_x:
            DMX[(i+1) * stevilo_tock_v_vrstici][0] = grid_poz_1_3_x*(i+1) + min(poz_3_x,poz_1_x)
            DMX[(i+1) * stevilo_tock_v_vrstici][1] = grid_poz_1_3_y*(i+1) + min(poz_3_y,poz_1_y)
        else:
            DMX[(i+1) * stevilo_tock_v_vrstici][0] = abs(grid_poz_1_3_x*(i+1) - max(poz_3_x,poz_1_x))
            DMX[(i+1) * stevilo_tock_v_vrstici][1] = grid_poz_1_3_y*(i+1) + min(poz_3_y,poz_1_y)

        # poz 2-4
        if poz_4_x > poz_2_x:
            DMX[((i+1)*stevilo_tock_v_vrstici) + stevilo_tock_v_vrstici-1][0] = grid_poz_2_4_x*(i+1) + min(poz_2_x,poz_4_x)
            DMX[((i+1)*stevilo_tock_v_vrstici) + stevilo_tock_v_vrstici-1][1] = grid_poz_2_4_y*(i+1) + min(poz_2_y,poz_4_y)
        else:
            DMX[((i+1)*stevilo_tock_v_vrstici) + stevilo_tock_v_vrstici-1][0] = abs(grid_poz_2_4_x*(i+1) - max(poz_2_x,poz_4_x))
            DMX[((i+1)*stevilo_tock_v_vrstici) + stevilo_tock_v_vrstici-1][1] = grid_poz_2_4_y*(i+1) + min(poz_2_y,poz_4_y)
    #print(DMX)
    
    # preračun preostalih koordinat
    for i in range(stevilo_tock_v_vrstici-2):
        for j in range(stevilo_tock_v_vrstici-2):
            # poenostavljen zapis 

            #        konc_vred
            #         ˇ
            #   |-----|
            #   |-----|
            #   |-----|
            #   |-----|
            #   ^
            #  zac_vred
            zac_vred_x = DMX[((i+1)*stevilo_tock_v_vrstici)][0]
            zac_vred_y = DMX[((i+1)*stevilo_tock_v_vrstici)][1]
            konc_vred_x = DMX[((i+1)*stevilo_tock_v_vrstici) + (stevilo_tock_v_vrstici-1)][0]
            konc_vred_y = DMX[((i+1)*stevilo_tock_v_vrstici) + (stevilo_tock_v_vrstici-1)][1]

            # Korak za katerega se koordinata povečuje s skrajnih leg
            grid_x = abs(zac_vred_x-konc_vred_x)/(stevilo_tock_v_vrstici-1)
            grid_y = abs(zac_vred_y-konc_vred_y)/(stevilo_tock_v_vrstici-1)        

            # izracun koordinat
            if zac_vred_x < konc_vred_x:
                DMX[((i+1)*stevilo_tock_v_vrstici) + (j+1)][0] = grid_x*(j+1) + min(zac_vred_x, konc_vred_x)  
            else:
                DMX[((i+1)*stevilo_tock_v_vrstici) + (j+1)][0] = abs(grid_x*(j+1) - max(zac_vred_x, konc_vred_x))
            if zac_vred_y < konc_vred_y: # SPREMENI CE ZAFRKAVA
                DMX[((i+1)*stevilo_tock_v_vrstici) + (j+1)][1] = grid_y*(j+1) + min(zac_vred_y, konc_vred_y) 
            else:
                DMX[((i+1)*stevilo_tock_v_vrstici) + (j+1)][1] = abs(grid_y*(j+1) - max(zac_vred_y, konc_vred_y))

    DMX = DMX.astype(int)
    return DMX


def ogljisca_slika(tocke = 5):
    stevilo_tock_v_vrstici = tocke
    stevilo_tock = stevilo_tock_v_vrstici**2
    slika = np.zeros((stevilo_tock,2))

    return slika


def Meshgrid_slika(pan1=0,pan2=0,pan3=0,pan4=0, tilt1=0,tilt2=0,tilt3=0,tilt4=0, tocke = 5):
    '''Funkcija sprejme koordinate luči "pan" in "tilt", ki jih dobimo z klikanjem ogljišč v GUI-u
    
    - argument_1: število točk v vrstici mreže, po kateri se bo luč zapeljala za kalibracijo
    - argument_2,3: pan, tilt
    '''
    # Ustvarimo število točk za MREŽO po kateri se bo peljala luč za kalibracijo
    stevilo_tock_v_vrstici = tocke
    stevilo_tock = stevilo_tock_v_vrstici**2

    DMX = np.zeros((stevilo_tock,2))
    DMX_calib = np.zeros((stevilo_tock,2))
    # Koordinate točk, ki še niso preračunane dobijo vrednost "nan"
    DMX[DMX == 0] = np.nan
    # Pozicije skrajnih točk - za vrstni red v matriki
    poz_1 = 0
    poz_2 = int(stevilo_tock_v_vrstici-1)
    poz_3 = int(stevilo_tock-stevilo_tock_v_vrstici)
    poz_4 = stevilo_tock-1
 
    
    DMX[poz_1] = pan1, tilt1
    DMX[poz_2] = pan2, tilt2
    DMX[poz_3] = pan3, tilt3
    DMX[poz_4] = pan4, tilt4

    # koordinate v skrajnih točkah - uporaba za enačbe ipd.
    poz_1_x = DMX[poz_1][0]
    poz_1_y = DMX[poz_1][1]
    poz_2_x = DMX[poz_2][0]
    poz_2_y = DMX[poz_2][1]
    poz_3_x = DMX[poz_3][0]
    poz_3_y = DMX[poz_3][1]
    poz_4_x = DMX[poz_4][0]
    poz_4_y = DMX[poz_4][1]

    # enačbe za MREŽO (izračun koordinat točk med ogljisci oz. pozicijami)

    # poz3        poz4
    #     |------|
    #     |      |
    #     |      |
    #     |------|
    # poz1        poz2

    grid_poz_1_2_x = abs(poz_2_x-poz_1_x)/(stevilo_tock_v_vrstici-1)
    grid_poz_1_2_y = abs(poz_2_y-poz_1_y)/(stevilo_tock_v_vrstici-1)

    grid_poz_3_4_x = abs(poz_4_x-poz_3_x)/(stevilo_tock_v_vrstici-1)
    grid_poz_3_4_y = abs(poz_4_y-poz_3_y)/(stevilo_tock_v_vrstici-1)

    grid_poz_1_3_x = abs(poz_3_x-poz_1_x)/(stevilo_tock_v_vrstici-1)
    grid_poz_1_3_y = abs(poz_3_y-poz_1_y)/(stevilo_tock_v_vrstici-1)

    grid_poz_2_4_x = abs(poz_2_x-poz_4_x)/(stevilo_tock_v_vrstici-1)
    grid_poz_2_4_y = abs(poz_2_y-poz_4_y)/(stevilo_tock_v_vrstici-1)

    # Preracun in zapis koordinat skrajnih točk mreže
    # DMX[pozicija v mrezi][koordinata x,y]

    for i in range(int(stevilo_tock_v_vrstici)-2):
        # poz 1-2
        if poz_2_x > poz_1_x:
            DMX[i+1][0] = grid_poz_1_2_x*(i+1) + min(poz_2_x,poz_1_x)
        else:
            DMX[i+1][0] = abs(grid_poz_1_2_x*(i+1) - max(poz_2_x,poz_1_x))
        if poz_2_y > poz_1_y: # SPREMENI ČE ZAFRKAVA
            DMX[i+1][1] = grid_poz_1_2_y*(i+1) + min(poz_2_y,poz_1_y)
        else:
            DMX[i+1][1] = abs(grid_poz_1_2_y*(i+1) - max(poz_2_y,poz_1_y))

        # poz 3-4
        if poz_4_x > poz_3_x:
            DMX[(i+1)+(stevilo_tock-stevilo_tock_v_vrstici)][0] = grid_poz_3_4_x*(i+1) + min(poz_3_x,poz_4_x)
        else:
            DMX[(i+1)+(stevilo_tock-stevilo_tock_v_vrstici)][0] = abs(grid_poz_3_4_x*(i+1) - max(poz_3_x,poz_4_x))
        if poz_3_y < poz_4_y:
            DMX[(i+1)+(stevilo_tock-stevilo_tock_v_vrstici)][1] = grid_poz_3_4_y*(i+1) + min(poz_3_y,poz_4_y)
        else:
            DMX[(i+1)+(stevilo_tock-stevilo_tock_v_vrstici)][1] = abs(grid_poz_3_4_y*(i+1) - max(poz_3_y,poz_4_y))

        # poz 1-3
        if poz_3_x > poz_1_x:
            DMX[(i+1) * stevilo_tock_v_vrstici][0] = grid_poz_1_3_x*(i+1) + min(poz_3_x,poz_1_x)
            DMX[(i+1) * stevilo_tock_v_vrstici][1] = grid_poz_1_3_y*(i+1) + min(poz_3_y,poz_1_y)
        else:
            DMX[(i+1) * stevilo_tock_v_vrstici][0] = abs(grid_poz_1_3_x*(i+1) - max(poz_3_x,poz_1_x))
            DMX[(i+1) * stevilo_tock_v_vrstici][1] = grid_poz_1_3_y*(i+1) + min(poz_3_y,poz_1_y)

        # poz 2-4
        if poz_4_x > poz_2_x:
            DMX[((i+1)*stevilo_tock_v_vrstici) + stevilo_tock_v_vrstici-1][0] = grid_poz_2_4_x*(i+1) + min(poz_2_x,poz_4_x)
            DMX[((i+1)*stevilo_tock_v_vrstici) + stevilo_tock_v_vrstici-1][1] = grid_poz_2_4_y*(i+1) + min(poz_2_y,poz_4_y)
        else:
            DMX[((i+1)*stevilo_tock_v_vrstici) + stevilo_tock_v_vrstici-1][0] = abs(grid_poz_2_4_x*(i+1) - max(poz_2_x,poz_4_x))
            DMX[((i+1)*stevilo_tock_v_vrstici) + stevilo_tock_v_vrstici-1][1] = grid_poz_2_4_y*(i+1) + min(poz_2_y,poz_4_y)
    #print(DMX)
    
    # preračun preostalih koordinat
    for i in range(stevilo_tock_v_vrstici-2):
        for j in range(stevilo_tock_v_vrstici-2):
            # poenostavljen zapis 

            #        konc_vred
            #         ˇ
            #   |-----|
            #   |-----|
            #   |-----|
            #   |-----|
            #   ^
            #  zac_vred
            zac_vred_x = DMX[((i+1)*stevilo_tock_v_vrstici)][0]
            zac_vred_y = DMX[((i+1)*stevilo_tock_v_vrstici)][1]
            konc_vred_x = DMX[((i+1)*stevilo_tock_v_vrstici) + (stevilo_tock_v_vrstici-1)][0]
            konc_vred_y = DMX[((i+1)*stevilo_tock_v_vrstici) + (stevilo_tock_v_vrstici-1)][1]

            # Korak za katerega se koordinata povečuje s skrajnih leg
            grid_x = abs(zac_vred_x-konc_vred_x)/(stevilo_tock_v_vrstici-1)
            grid_y = abs(zac_vred_y-konc_vred_y)/(stevilo_tock_v_vrstici-1)        

            # izracun koordinat
            if zac_vred_x < konc_vred_x:
                DMX[((i+1)*stevilo_tock_v_vrstici) + (j+1)][0] = grid_x*(j+1) + min(zac_vred_x, konc_vred_x)  
            else:
                DMX[((i+1)*stevilo_tock_v_vrstici) + (j+1)][0] = abs(grid_x*(j+1) - max(zac_vred_x, konc_vred_x))
            if zac_vred_y < konc_vred_y: # SPREMENI CE ZAFRKAVA
                DMX[((i+1)*stevilo_tock_v_vrstici) + (j+1)][1] = grid_y*(j+1) + min(zac_vred_y, konc_vred_y) 
            else:
                DMX[((i+1)*stevilo_tock_v_vrstici) + (j+1)][1] = abs(grid_y*(j+1) - max(zac_vred_y, konc_vred_y))

    DMX = DMX.astype(int)
    return DMX
