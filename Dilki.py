
"""
NOTLAR:
    Bos sutunlarimi doldurmam lazim.

    Program inanilmaz sekilde hantal belki de bozuk
"""



import sqlite3

#----------------------------------------------------------------------------------------------------------------------
#HeceEk klasi                                                                                                         #
#______________________________________________________________________________________________________________________
class HeceEk():



    #HARFLER_____________________________________________________________________________________________________________
    ##Seli Harfler:
    sesli_harfler= "a", "e", "ı", "i", "o", "ö", "u", "ü"
    sessiz_harfler= "b", "c", "ç", "d", "f", "g", "ğ", "h", "k", "l", "m", "n", "p", "r", "s", "ş", "t", "v", "y", "z"



    #HAVUZLAR____________________________________________________________________________________________________________
    eksik_heceler = e_h = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
    ##Kok Heceler:
    kok_heceler = k_h = []
    ##Gizli Kavusuk Heceler:
    gizli_kavusuk_heceler = g_k_h = []
    ##Acik Kavusuk Heceler:
    acik_kavusuk_heceler = a_k_h = []
    """#IKI HECELILER
    Iki heceliler:
            1) k_h + k_h
            2) k_h + g_k_h
            3) k_h + a_k_h
            4) k_h + e_h

            5) g_k_h + g_k_h
            6) g_k_h + a_k_h
            7) g_k_h + e_h
            8) g_k_h + k_h

            9)  a_k_h + a_k_h
            10) a_k_h + e_h
            11) a_k_h + k_h
            12) a_k_h + g_k_h

            13) e_h + e_h
            14) e_h + k_h
            15) e_h + g_k_h
            16) e_h + a_k_h

    Bunlar iki heceliler listesi icindeki listelerde numara sirasina gore yer alacaklar """



    tek_heceliler = [k_h, g_k_h, a_k_h, e_h]
    iki_heceliler = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]



    #FONKSIYONLARIM___________________________________________________________________________________________________________
    def dosyala(sirasi, iclemi, dosya_adi, iclekledigi_liste, turu="doc", calisimi="w", alfabetik=False, tekrari_yoket=False):
        isim = str(sirasi + ") " + iclemi + ") " + dosya_adi + "." + turu)
        listeadi_dosyam = open(isim,calisimi,encoding="utf-8")
        if tekrari_yoket == True:
            iclekledigi_liste = set(iclekledigi_liste)
            iclekledigi_liste = list(iclekledigi_liste)
        if alfabetik == True:
            iclekledigi_liste.sort()
        listeadi_dosyam.write(str(iclekledigi_liste))
        listeadi_dosyam.close()

    def iki_heceli_oldur_kalip(ilk_kategori, ikinci_kategori, ic_liste_numarasi, dosya_adi, kucuk_harfi, dosyala=True, buyuk_harfi = "B"):
        for donut1 in range(len(ilk_kategori)):
            for donut2 in range(len(ikinci_kategori)):
                HeceEk.iki_heceliler[ic_liste_numarasi] += [ilk_kategori[donut1] + ikinci_kategori[donut2]]
        if dosyala == True:
            HeceEk.dosyala(buyuk_harfi, kucuk_harfi, dosya_adi, HeceEk.iki_heceliler[ic_liste_numarasi])

    #ILK HECELER_______________________________________________________________________________________________________________
    def kok_hece_oldur(dosyala=False):
        for sira in range(len(HeceEk.sessiz_harfler)):
            for sira2 in range(len(HeceEk.sesli_harfler)):
                HeceEk.kok_heceler += [HeceEk.sesli_harfler[sira2]+HeceEk.sessiz_harfler[sira]]
        if dosyala == True:
            HeceEk.dosyala("A","a","Kök Heceler",HeceEk.kok_heceler)

    def gizli_kavusuk_heceler_oldur(dosyala=False):
        for sira1 in range(len(HeceEk.sessiz_harfler)):
            for sira22 in range(len(HeceEk.sesli_harfler)):
                HeceEk.gizli_kavusuk_heceler += [HeceEk.sessiz_harfler[sira1]+HeceEk.sesli_harfler[sira22]]
        if dosyala == True:
            HeceEk.dosyala("A","b","Gizli Kavuşuk Heceler",HeceEk.gizli_kavusuk_heceler)

    def acik_kavusuk_heceler_oldur(dosyala=False):
        for sira11 in range(len(HeceEk.sessiz_harfler)):
            for sira222 in range(len(HeceEk.sesli_harfler)):
                for sira3 in range(len(HeceEk.sessiz_harfler)):
                    HeceEk.acik_kavusuk_heceler += [HeceEk.sessiz_harfler[sira11]+HeceEk.sesli_harfler[sira222] + HeceEk.sessiz_harfler[sira3]]
        if dosyala == True:
            HeceEk.dosyala("A","c","Açık Kavuşuk Heceler",HeceEk.acik_kavusuk_heceler)

    def eksik_heceliler_oldur(dosyala=False):
        if dosyala == True:
            HeceEk.dosyala("A","ç","Eksik Heceliler",HeceEk.e_h)

    def tek_heceliler_oldur():
        HeceEk.kok_hece_oldur()
        HeceEk.gizli_kavusuk_heceler_oldur()
        HeceEk.acik_kavusuk_heceler_oldur()
        HeceEk.eksik_heceliler_oldur()

    #IKI HECELILER________________________________________________________________________________________________________________
    def iki_heceliler_oldur():
        HeceEk.iki_heceli_oldur_kalip(HeceEk.k_h, HeceEk.k_h, 0, "k_h + k_h", "a",dosyala=False)
        HeceEk.iki_heceli_oldur_kalip(HeceEk.k_h, HeceEk.g_k_h, 1, "k_h + g_k_h", "b",dosyala=False)
        HeceEk.iki_heceli_oldur_kalip(HeceEk.k_h, HeceEk.a_k_h, 2, "k_h + a_k_h", "c",dosyala=False)
        HeceEk.iki_heceli_oldur_kalip(HeceEk.k_h, HeceEk.e_h, 3, "k_h + e_h", "ç",dosyala=False)

        HeceEk.iki_heceli_oldur_kalip(HeceEk.g_k_h, HeceEk.g_k_h, 4, "g_k_h + g_k_h", "d",dosyala=False)
        HeceEk.iki_heceli_oldur_kalip(HeceEk.g_k_h, HeceEk.a_k_h, 5, "g_k_h + a_k_h", "e",dosyala=False)
        HeceEk.iki_heceli_oldur_kalip(HeceEk.g_k_h, HeceEk.e_h, 6, "g_k_h + e_h", "f",dosyala=False)
        HeceEk.iki_heceli_oldur_kalip(HeceEk.g_k_h, HeceEk.k_h, 7, "g_k_h + k_h" , "g",dosyala=False)

        HeceEk.iki_heceli_oldur_kalip(HeceEk.a_k_h, HeceEk.a_k_h, 8, "a_k_h + a_k_h", "ğ",dosyala=False)
        HeceEk.iki_heceli_oldur_kalip(HeceEk.a_k_h, HeceEk.e_h, 9, "a_k_h + e_h", "h",dosyala=False)
        HeceEk.iki_heceli_oldur_kalip(HeceEk.a_k_h, HeceEk.k_h, 10, "a_k_h + k_h", "ı",dosyala=False)
        HeceEk.iki_heceli_oldur_kalip(HeceEk.a_k_h, HeceEk.g_k_h, 11, "a_k_h + g_k_h", "i",dosyala=False)

        HeceEk.iki_heceli_oldur_kalip(HeceEk.e_h, HeceEk.e_h, 12, "e_h + e_h", "j",dosyala=False)
        HeceEk.iki_heceli_oldur_kalip(HeceEk.e_h, HeceEk.k_h, 13, "e_h + k_h", "k",dosyala=False)
        HeceEk.iki_heceli_oldur_kalip(HeceEk.e_h, HeceEk.g_k_h, 14, "e_h + g_k_h", "l",dosyala=False)
        HeceEk.iki_heceli_oldur_kalip(HeceEk.e_h, HeceEk.a_k_h, 15, "e_h + a_k_h", "m",dosyala=False)

#----------------------------------------------------------------------------------------------------------------------------------------
#VeriDiz klasi                                                                                                                          #
#________________________________________________________________________________________________________________________________________
class VeriDiz():
    def buukk(kelime):
        # buyuk unlu uyumu kanlik kontrolu
        sesliler = s = "a", "ı", "u", "o", "e", "i", "ü", "ö"
        kalin_unluler = ku = "a", "ı", "u", "o"
        ince_unluler = iu = "e", "i", "ü", "ö"

        kelimenin_seslileri = ks = []

        deney_tupu_ince = dti = 0
        deney_tupu_kalin = dtk = 0

        for harf in kelime:
            if harf in s:
                ks += harf
        if len(ks) >= 2:
            for nesne in ks:
                if nesne in iu:
                    dti += 1
                elif nesne in ku:
                    dtk += 1

            if dti > 0:
                return "H"
            if dti <= 0:
                return "E"
        elif len(ks) <= 1:
            return "n"

    def buuik(kelime):
        # buyuk unlu uyumu incelik kontrolu
        sesliler = s = "a", "ı", "u", "o", "e", "i", "ü", "ö"
        kalin_unluler = ku = "a", "ı", "u", "o"
        ince_unluler = iu = "e", "i", "ü", "ö"

        kelimenin_seslileri = ks = []

        deney_tupu_ince = dti = 0
        deney_tupu_kalin = dtk = 0

        for harf in kelime:
            if harf in s:
                ks += harf
        if len(ks) >= 2:
            for nesne in ks:
                if nesne in iu:
                    dti += 1
                elif nesne in ku:
                    dtk += 1

            if dtk > 0:
                return "H"
            if dtk <= 0:
                return "E"
        elif len(ks) <= 1:
            return "n"

    def buuk(kelime):
        # buyuk unlu uyumu kontrolu
        sesliler = s = "a", "ı", "u", "o", "e", "i", "ü", "ö"
        kalin_unluler = ku = "a", "ı", "u", "o"
        ince_unluler = iu = "e", "i", "ü", "ö"

        kelimenin_seslileri = ks = []

        deney_tupu_ince = dti = 0
        deney_tupu_kalin = dtk = 0

        for harf in kelime:
            if harf in s:
                ks += harf
        if len(ks) >= 2:
            for nesne in ks:
                if nesne in iu:
                    dti += 1
                elif nesne in ku:
                    dtk += 1

            if dtk >= 1:
                if dti >= 1:
                    return "H"

            if dtk >= 1:
                if dti == 0:
                    return "E"
            if dti >= 1:
                if dtk == 0:
                    return "E"
        elif len(ks) <= 1:
            return "n"

    def kuudk(kelime):
        # kucuk unlu uyumu -duzden- kontrolu
        duz = "a", "e", "ı", "i"

        kelimeninsesliler = ks = []
        duzlu = []
        diger = []

        for harf in kelime:
            if harf in HeceEk.sesli_harfler:
                ks += [harf]

        for sesli in ks:
            if sesli in duz:
                duzlu += [sesli]
            else:
                diger += [sesli]
        if len(ks) >= 2:
            if len(duzlu) >= 1:
                if len(diger) ==0:
                    return "E"
            if len(duzlu) ==0:
                    return "H"
            if len(duzlu) >= 1:
                if len(diger) >= 1:
                    return "H"
        elif len(ks) <= 1:
            return "n"

    def kuuy1k(kelime):
        # kucuk unlu uyumu -yuvarlakdan 1- kontrolu
        duz_unluler          = "a", "e", "ı", "i"
        yuvarlak_unluler     = "o", "ö", "u", "ü"
        dar_yuvarlak_unluler = "u", "ü"

        kelimeninsesliler  = ks  = []
        ilk_sesli          = ils = []
        ikinci_sesli       = iks = []

        for harf in kelime:
            if harf in HeceEk.sesli_harfler:
                ks += [harf]

        ils += [ks[0]]
        if len(ks)>1:
            iks += [ks[1]]

        if len(ks) >= 2:
            if ils[0] in duz_unluler:
                return "H"
            elif ils[0] in yuvarlak_unluler:
                if iks[0] in dar_yuvarlak_unluler:
                    return "E"
                elif iks[0] not in dar_yuvarlak_unluler:
                    return "H"
        elif len(ks) == 1:
            return "n"

    def kuuy2k(kelime):
        # kucuk unlu uyumu -yuvarlakdan 1- kontrolu
        duz_unluler          = "a", "e", "ı", "i"
        yuvarlak_unluler     = "o", "ö", "u", "ü"
        duz_genis_unluler    = "a", "e"

        kelimeninsesliler  = ks  = []
        ilk_sesli          = ils = []
        ikinci_sesli       = iks = []

        for harf in kelime:
            if harf in HeceEk.sesli_harfler:
                ks += [harf]

        ils += [ks[0]]
        if len(ks)>1:
            iks += [ks[1]]

        if len(ks) >= 2:
            if ils[0] in duz_unluler:
                return "H"
            elif ils[0] in yuvarlak_unluler:
                if iks[0] in duz_genis_unluler:
                    return "E"
                elif iks[0] not in duz_genis_unluler:
                    return "H"
        elif len(ks) == 1:
            return "n"


    def u_i_s(kelimeu):
        # uyum incelenim sorgula
        sesli= "a","e","ı","i","u","ü","o","ö"
        sayac = 0
        for harf in kelimeu:
            if harf in sesli:
                sayac += 1
        if sayac >1:
            return "E"
        else:
            return "H"

    def hla(rakam1, rakam2):
        #hece liste adi
        rakam1 = rakam1 - 1
        rakam2 = rakam2 - 1

        listeler_ust = l_u = ["tek heceliler", "cift heceliler"]

        listeler_listesi_str = llstr = ["kok hece", "gizli kavusuk hece", "acik kavusuk hece", "eksik hece", "k_h + k_h", "k_h + g_k_h", "k_h + a_k_h", "k_h + e_h",
                                        "g_k_h + g_k_h", "g_k_h + a_k_h", "g_k_h + e_h", "g_k_h + k_h", "a_k_h + a_k_h", "a_k_h + e_h", "a_k_h + k_h", "a_k_h + g_k_h",
                                        "e_h + e_h", "e_h + k_h", "e_h + g_k_h", "e_h + a_k_h"]
        return str(l_u[rakam1]) + """ / """ + str(llstr[rakam2])



    def veri_yaz():
        listeler_listesi = l_l = [HeceEk.tek_heceliler, HeceEk.iki_heceliler]

        veri_tabani = v_t = sqlite3.connect("Havuz.sqlite3")

        imlec = im = v_t.cursor()

        im.execute("""CREATE TABLE IF NOT EXISTS Dil (Hecesel_Sinif, Kelime_No, Kelime, Birimleri, Baglayicilari, Birim_Sayisi, Baglayici_Sayisi, Harf_Sayisi, Uyum_Incelenim_Imkani, BUU_kalinlik, BUU_incelik, Buyuk_unlu_Uyumlu, KUU_dd, KUU_y1, KUU_y2)""")

        ## Geriye kalan bos bilgiler;
        ## Uyumlar K = Kucuk_unlu_Uyumlu
        ## Imla      = Imlada_Bulunakligi

        sayacn = 0

        sayac_ust_liste = s_u_l = 0
        sayac_alt_liste = s_a_l = 0

        for ust_liste in l_l:
            s_u_l += 1
            for alt_liste in ust_liste:
                s_a_l += 1
                for veri in alt_liste:
                    sayacn += 1
                    im.execute(f"""INSERT INTO Dil VALUES("{VeriDiz.hla(s_u_l, s_a_l)}", "{sayacn}", "{veri}", "{[i for i in veri if i not in HeceEk.sesli_harfler]}", "{[i for i in veri if i not in HeceEk.sessiz_harfler]}", "{len([i for i in veri if i not in HeceEk.sesli_harfler])}", "{len([i for i in veri if i not in HeceEk.sessiz_harfler])}", "{len([i for i in veri])}", "{VeriDiz.u_i_s(veri)}","{VeriDiz.buukk(veri)}", "{VeriDiz.buuik(veri)}", "{VeriDiz.buuk(veri)}", "{VeriDiz.kuudk(veri)}", "{VeriDiz.kuuy1k(veri)}", "{VeriDiz.kuuy2k(veri)}")""")

        v_t.commit()
        v_t.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Gosteri klasi                                                                                                                                               #
#_____________________________________________________________________________________________________________________________________________________________
class Gosteri():
    def emir():
        #Ilk Oldurlar:
        HeceEk.tek_heceliler_oldur()
        HeceEk.iki_heceliler_oldur()
        #Ikinci Oldurlar:
        VeriDiz.veri_yaz()
        #Ekran
        print("bitti")

Gosteri.emir()
