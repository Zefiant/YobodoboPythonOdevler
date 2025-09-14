"""
Bir sınıfta öğrencilerin bilgilerini tutan küçük bir öğrenci yönetim sistemi yazacaksınız. 
Sistem şu işlemleri yapacak: öğrenci ekleme, listeleme, arama, basit istatistikler ve 
raporlama. 
Amaç, derslerde öğrendiğimiz veri tipleri ve kontrol yapılarını gerçek bir senaryo içinde 
kullanmak.
"""

#Sınıfın değerleri atandı
sinif_adi = "Python Eğitim Sınıfı"
sinif_mvct_ogr_sayisi = 4
sinif_ort_basari_puani = 50.0
aktif_mi = True

#Öğrenci sözlükleri oluşturuldu
ogrenci1 = {
    "isim" : "AHMET"
    ,"yas" : 18
    ,"not" : 40
}

ogrenci2 = {
    "isim" : "MEHMET"
    ,"yas" : 19
    ,"not" : 50
}

ogrenci3 = {
    "isim" : "YAHYA"
    ,"yas" : 20
    ,"not" : 60
}

ogrenci4 = {
    "isim" : "SAMET"
    ,"yas" : 21
    ,"not" : 70
}

#Sözlükler listeye atıldı
ogrenciler = [ogrenci1,ogrenci2,ogrenci3,ogrenci4]

#Çıkış yapılana kadar işlemlerin devam etmesi için while ile sonsuz döngü yapıldı
while True:
    secim = int(input("""
o 1. Öğrenci Ekle 
o 2. Öğrencileri Listele 
o 3. Öğrenci Ara 
o 4. İstatistikler 
o 5. Çıkış     
Lütfen bir numara seçiniz: """))
    
    #Yapılan seçim kullanıcıya gösterildi ve seçime göre if blokları ile işlemler yapıldı
    print(f"Seçiminiz: {secim}")
    if secim == 1:

        #Yeni öğrenci ekleme
        eklenecek_ogrencinin_ismi = input("Eklemek istediğiniz öğrencinin ismini giriniz: ").upper()
        eklenecek_ogrencinin_yasi= int(input("Eklemek istediğiniz öğrencinin yaşını giriniz: "))
        eklenecek_ogrencinin_notu = int(input("Eklemek istediğiniz öğrencinin notunu giriniz: "))

        yeniogrenci = {
            "isim" : eklenecek_ogrencinin_ismi
            ,"yas" : eklenecek_ogrencinin_yasi
            ,"not" : eklenecek_ogrencinin_notu
        }

        #Değerler kullanıcıdan alınarak sözlük haline getirilip listeye eklendi
        ogrenciler.append(yeniogrenci)

        if  eklenecek_ogrencinin_notu > sinif_ort_basari_puani :
            durum = "Geçti"
        else:
            durum = "Kaldı"

        print(f"Öğrenci başarıyla eklenmiştir. (Durum: {durum})")
    elif secim == 2:

        #Tüm öğrencileri listeleme
        print("Öğrenciler:")
        for ogrenci in ogrenciler:
            print(f"-{ogrenci["isim"]} ({ogrenci["yas"]} yaşında) -> Not: {ogrenci["not"]}\t")
    elif secim == 3:

        #Girilen isimdeki tüm öğrencileri listeler
        aranan_ogrenci_ismi = input("Aramak istediğiniz öğrencinin ismini giriniz: ").upper()
        print(f"{aranan_ogrenci_ismi} isimli öğrenci/ler:")
        for ogrenci in ogrenciler:
            if ogrenci["isim"] != aranan_ogrenci_ismi:
                continue
            print(f"-{ogrenci["isim"]} ({ogrenci["yas"]} yaşında) -> Not: {ogrenci["not"]}\t")
    elif secim == 4:

        #İstatistik işlemleri yapılır, ortalama, en yüksek - en düşük not, geçen namükerrer öğrenci isimleri
        not_toplami = 0
        en_yuksek_not = 0
        en_dusuk_not = 100
        for ogrenci in ogrenciler:
            ogrenci_not = ogrenci["not"]

            not_toplami += ogrenci_not
            if ogrenci_not > en_yuksek_not:
                en_yuksek_not = ogrenci_not

            if ogrenci_not < en_dusuk_not:
                en_dusuk_not = ogrenci_not
        not_ortalamasi = not_toplami / len(ogrenciler)

        #List Comprehension  
        gecen_ogrenci_isimleri = {ogrenci["isim"] for ogrenci in ogrenciler if ogrenci["not"] > sinif_ort_basari_puani} #set
        notlarin_karesi = [ogrenci["not"]**2 for ogrenci in ogrenciler]

        print(f"Tüm öğrencilerin not ortalaması -> {not_ortalamasi}")
        print(f"En yüksek not-> {en_yuksek_not}")
        print(f"En düşük not -> {en_dusuk_not}")
        print(f"Geçen namükerrer öğrenciler -> {gecen_ogrenci_isimleri}")

    elif secim == 5:

        #Çıkış
        print("Çıkış yapılıyor...")
        break

    else:

        #Başka numara girilmesi durumunda önlem
        print("Lütfen bir numara seçiniz")
