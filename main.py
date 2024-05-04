#KUTUPHANELER
from datetime import datetime #tarih ve saati çekeceğimiz modül
import tkinter #GUI yapacağımız modül
import random #rastgele işlemlerini yapacağımız modül

#TARIH SAAT
tarihSaatGun = datetime.now()  #tarih ve saat bilgisini çekiyoruz
tarih = tarihSaatGun.strftime("%d.%m.%Y") #tarih bilgisine göre filtreliyoruz
saat = tarihSaatGun.strftime("%H:%M") #saat bilgisine göre filtreliyoruz
gun = tarihSaatGun.strftime("%A") #gün bilgisine göre filteriyoruz

#SOZLER
sozler = [


    "En büyük engeller, en büyük zaferlerin öncesindedir.",
    "Başarı, birçok kez düşmekten vazgeçmediğinizde ortaya çıkar.",
    "Zorluklar, kendinizi geliştirmenin fırsatlarıdır.",
    "Hayal kurun, inanın, başarın!",
    "Zorluklar, sizi daha güçlü kılar.",
    "Hayatta her adım, bir sonraki başarıya giden bir yolculuktur.",
    "Başarılı olmanın anahtarı, asla pes etmemektir.",
    "Her başarısızlık, bir sonraki başarıya giden bir adımdır.",
    "Geleceğinizi şekillendiren, bugünkü kararlarınızdır.",
    "Hayatta başarı, istikrarlı çaba ve inançla gelir.",
    "İmkansız, sadece yapılması biraz daha uzun süre alır.",
    "Her yeni gün, yeni bir başlangıçtır ve yeni fırsatlar sunar.",
    "Başarının tadını çıkarmak için her adımı takdir edin.",
    "Hayal edin, inanın, başarın!",
    "Bir hedefe ulaşmak için gereken en önemli şey, başlamaktır.",
    "Başarılı insanlar, engelleri fırsatlara dönüştürenlerdir.",
    "Her düşüş, daha güçlü bir şekilde kalkmanızı sağlar.",
    "Hayal kurun, cesaret edin, başarın!",
    "Her adım, büyük bir başarıya giden bir yolun parçasıdır.",
    "Hayatta her an, yeni bir fırsat sunar.",
    "Zorluklar, gücünüzü keşfetmenin bir yoludur.",
    "İnanın, başarın ve düşlerinize ulaşın!",
    "Başarı, sürekli çaba ve azim gerektirir.",
    "Yarının başarısı, bugünkü çabalarınıza bağlıdır.",
    "Her yeni gün, yeni bir fırsat ve yeni bir başlangıçtır.",
    "Başarı, engelleri aşma iradesidir.",
    "Kendinize olan güveniniz, sizi en yükseklere taşıyabilir.",
    "Başarı, azimle pes etmeden çalışmanın sonucudur.",
    "Yapabileceğinizi düşünürseniz, yapabilirsiniz!",
    "Başarı, sabır ve sürekli çaba gerektirir.",
    "Hayatta pes etmek yok, sadece daha fazla deneme var.",
    "Her adım, hedefinize biraz daha yaklaşmanızı sağlar.",
    "Engeller sizi durdurmasın, sizi daha da güçlü kılsın.",
    "Unutmayın, hayal edebildiğiniz her şeyi başarabilirsiniz!"
]

#GUNLER CEVIRI
if gun =="Monday":
    gun = "Pazartesi"
elif gun =="Tuesday":
    gun = "Salı"
elif gun =="Wednesday":
    gun = "Çarşamba"
elif gun =="Thursday":
    gun = "Perşembe"
elif gun =="Friday":
    gun = "Cuma"
elif gun =="Saturday":
    gun = "Cumartesi"
elif gun =="Sunday":
    gun = "Pazar"

print(f"Şu anki tarih : {tarih}")
print(f"Şu anki saat : {saat}")
print(f"Şu anki gün : {gun}")


#GUI ARAYUZ
root = tkinter.Tk() #pencere oluştur
root.title("PYTHON GUI CLOCK") #pencere adı
root.geometry("525x215")#pencere boyutu
icon = tkinter.PhotoImage(file ="clock.png")#pencere ikonu
root.iconphoto(False,icon)#pencere ikonunu kullan
root.configure(bg="black")#pencere arkaplanı
root.attributes('-topmost',True)#pencereyi üstte tut
root.lift()#pencereyi üstte tut
root.minsize(450, 120)#minimum boyut
root.maxsize(525,215)#maksimum boyut

colortrans=False
minr=False

#FONTS
FONT = ("Comic Sans MS", 20, "bold")
FONTKUCUK = ("Comic Sans MS", 13, "bold")
FONTTARIH = ("Courier New", 15, "bold")
FONTSAAT=("ds-digital", 90)
FONTSOZLER =("Courier New",11 )
FONTGUN = ("Courier New", 13, "bold")


def writeClock(): #saati anlık olarak yazdırma kodu
    suan = datetime.now()
    filtre = suan.strftime("%H %M %S")
    saatLbl.config(text=filtre)
    root.after(1000,writeClock)

def randomsozler():
    return random.choice(sozler)# sözlerden rastgele seçiyor
print(randomsozler())

def invcolor(event): #renkleri tersine çevirme fonksiyonu
    global colortrans
    if colortrans==False:
        colortrans=True
        root.config(background="white")
        saatLbl.config(background="white")
        tarihLbl.config(background="white")
        sozlerLbl.config(background="white")
        bugunLbl.config(background="white")

    elif colortrans==True:
        colortrans=False
        root.config(background="black")
        saatLbl.config(background="black")
        tarihLbl.config(background="black")
        sozlerLbl.config(background = "black")
        bugunLbl.config(background="black")

def minroot(event): #pencere küçültme fonksiyonu
    global minr
    if minr==False:
        minr = True
        root.geometry("450x120")#minsize
    elif minr==True:
        minr = False
        root.geometry("525x215")#default


#UYGULAMA

#saat
saatLbl = tkinter.Label(root,font=FONTSAAT,bg="black",foreground="dark turquoise")
saatLbl.pack(anchor="center")#ekran merkezine yazdırma
writeClock()#saati yazdırma fonksiyonu

#tarih
tarihLbl = tkinter.Label(root, text=tarih, font=FONTTARIH, background="black", foreground="blue")
tarihLbl.pack()#ekrana yazdırma

#gun
bugunLbl = tkinter.Label(root, text=gun, font=FONTGUN, background="black", foreground="blue")
bugunLbl.pack()#ekrana yazdırma

#sozler
sozlerLbl = tkinter.Label(root,text=randomsozler(), font=FONTSOZLER, background="black",foreground="blue")
sozlerLbl.pack()#ekrana yazdırma

root.bind("<Button-1>", minroot)#sol tık
root.bind("<Button-3>", invcolor)#sağ tık


root.mainloop()#uygulamanın çalışması

