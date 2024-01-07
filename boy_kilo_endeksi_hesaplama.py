import tkinter

#window codes
window = tkinter.Tk()
window.title("BKE HESAPLAYICI")
window.minsize(300,250)

FONT=("Arial",15,"normal")

#BKE Hesaplama Fonksiyonu
def bke_hesaplama():
    boy = boy_input.get()
    kilo = kilo_input.get()
    if kilo== "" or boy == "":
        cevap_metin.config(text="Boyunuzu ve kilonuzu tam olarak girdiğinizden emin olunuz!")
    else:
        try:
            bke = float(boy) / ((float(kilo) / 100) ** 2)
            bke_cevap = bke_hesap(bke)
            cevap_metin.config(text=bke_cevap)
        except:
            cevap_metin.config(text="Bir numara giriniz!")


    

#Button and entry codes
boy= tkinter.Label(text="Boyunuzu giriniz: ",font=FONT)
boy.pack()
boy_input = tkinter.Entry(width=10)
boy_input.pack()

kilo = tkinter.Label(text="Kilonuzu giriniz: ",font=FONT)
kilo.pack()
kilo_input = tkinter.Entry(width=10)
kilo_input.pack()

hesapla_tus = tkinter.Button(text="Hesapla", command=bke_hesaplama)
hesapla_tus.pack()

cevap_metin = tkinter.Label()
cevap_metin.pack()


#Write the results
def bke_hesap(bke):
    bke_cevap=f"Boy kilo endeksiniz {round(bke,2)}, Sizin durumunuz:"
    
    if bke <= 16:
        bke_cevap += "Asiri Zayif"
    
    elif 16 < bke <= 17:
        bke_cevap += "Zayıf!"
    
    elif 17 < bke <= 18.5:
        bke_cevap += "Ideal!"

    elif 18.5 < bke <= 25:
        bke_cevap += "Kilolu!"
    else:
        bke_cevap += "OBEZ!!!!"
    return bke_cevap

    

window.mainloop()