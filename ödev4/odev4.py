import sqlite3

conn = sqlite3.connect('metinler.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS metin (
                    id INTEGER PRIMARY KEY,
                    icerik TEXT
                )''')


metin1 = input("Lütfen ilk metni girin: ")
metin2 = input("Lütfen ikinci metni girin: ")

cursor.execute("INSERT INTO metin (icerik) VALUES (?)", (metin1,))
cursor.execute("INSERT INTO metin (icerik) VALUES (?)", (metin2,))


conn.commit()

def dice_katsayisi_bi_gram(metin1, metin2):
    
    def bi_gram_olustur(metin):
        bi_gramlar = set()
        for i in range(len(metin) - 1):
            bi_gramlar.add(metin[i:i+2])
        return bi_gramlar
    
    
    bi_gramlar1 = bi_gram_olustur(metin1)
    bi_gramlar2 = bi_gram_olustur(metin2)
    
  
    kesisim = len(bi_gramlar1.intersection(bi_gramlar2))
    toplam_bi_gram_sayisi = len(bi_gramlar1) + len(bi_gramlar2)
    
    
    benzerlik_orani = (2 * kesisim) / toplam_bi_gram_sayisi
    
    return benzerlik_orani


benzerlik_orani = dice_katsayisi_bi_gram(metin1, metin2)


print(f"Metinler arasındaki benzerlik oranı (Dice Katsayısı): {benzerlik_orani:.2f}")

with open("benzerlik_durumu.txt", "w") as dosya:
    dosya.write(f"Metinler arasındaki benzerlik oranı (Dice Katsayısı): {benzerlik_orani:.2f}")


conn.close()
