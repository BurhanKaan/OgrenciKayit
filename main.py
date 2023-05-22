import tkinter as tk

Isim = []
Soyisim = []
Kimlikno = []
Ilce = ["Alpu","Beylikova","Çifteler","Günyüzü","Han","İnönü","Mahmudiye","Mihalgazi","Mihalıççık","Tepebaşı","Sarıcakaya","Seyitgazi","Sivrihisar","Odunpazarı"]
Okul = []
Cinsiyet = ["Erkek", "Kız"]
Sinif = ["9", "10", "11", "12"]

def KAYDET():
    Isim = isim.get
    Soyisim = soyisim.get
    Kimlikno = kimlikno.get
    Okul = okul.get
    Ilce = seciliilce.get()
    Cinsiyet = secilicinsiyet.get()
    Sinif = secilisinif.get()
    Bildirim_LABEL.config(text="Başarıyla Kaydedildi", fg="Green")

def TEMIZLE():
    isim.delete(0, tk.END)
    soyisim.delete(0, tk.END)
    kimlikno.delete(0, tk.END)
    okul.delete(0, tk.END)
    Bildirim_LABEL.config(text="Temizlendi", fg="grey")

window = tk.Tk()
window.title("Ders İçi Kimlik Sistemi")
window.config(width=1000, height=800)

Baslik = tk.Label(text="Ders İçi Kayıt Sistemi", bg="grey")
Baslik.place(x=0, y=0, height=30, width=1000)
CIKIS_btn = tk.Button(text="Çıkış", font="Arial 9", command=quit)
CIKIS_btn.place(x=945, y=3, width=50, height=25)

isim = tk.Entry(font="Arial 14")
isim.place(x=100, y=50, width=200, height=35)
isim_LABEL = tk.Label(text="İsim :", font="Arial 14")
isim_LABEL.place(x=45, y=50)

soyisim = tk.Entry(font="Arial 14")
soyisim.place(x=100, y=90, width=200, height=35)
soyisim_LABEL = tk.Label(text="Soyisim :", font="Arial 14")
soyisim_LABEL.place(x=15, y=90)

kimlikno = tk.Entry(font="Arial 14")
kimlikno.place(x=100, y=130, width=200, height=35)
kimlikno_LABEL = tk.Label(text="Kimlik No :", font="Arial 14")
kimlikno_LABEL.place(x=5, y=130)

seciliilce = tk.StringVar(window)
seciliilce.set(Ilce[0])
om_Ilce = tk.OptionMenu(window,seciliilce,*Ilce)
om_Ilce.place(x=100, y=170, width=200, height=35)
ilce_LABEL = tk.Label(text="İlçe :", font="Arial 14")
ilce_LABEL.place(x=54, y=170)

okul = tk.Entry(font="Arial 14")
okul.place(x=700, y=50, width=200, height=35)
okul_LABEL = tk.Label(text="Okul :", font="Arial 14")
okul_LABEL.place(x=640, y=50)

secilicinsiyet = tk.StringVar(window)
secilicinsiyet.set(Cinsiyet[0])
om_cinsiyet = tk.OptionMenu(window,secilicinsiyet,*Cinsiyet)
om_cinsiyet.place(x=700, y=90, width=200, height=35)
cinsiyet_LABEL = tk.Label(text="Cinsiyet :", font="Arial 14")
cinsiyet_LABEL.place(x=613, y=90)

sinif_LABEL = tk.Label(text="Sınıf :", font="Arial 14")
sinif_LABEL.place(x=640, y=130)
secilisinif = tk.StringVar(window)
secilisinif.set(Sinif[0])
om_sinif = tk.OptionMenu(window,secilisinif,*Sinif)
om_sinif.place(x=700, y=130, width=200, height=35)

Kayit = tk.Button(text="Kaydet", font="Arial 14", bg="blue", command=KAYDET)
Kayit.place(x=695, y=170, width=100, height=35)

Bildirim_LABEL = tk.Label(text="...", fg="black", font="Arial 14")
Bildirim_LABEL.place(x=695, y=220)

Temizle = tk.Button(text="Temizle", font="Arial 14", bg="grey", command=TEMIZLE)
Temizle.place(x=805, y=170, width=100, height=35)
window.mainloop()