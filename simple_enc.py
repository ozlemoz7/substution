
# SİMPLE SUBSTUTİON CHİPPER

# alfabe = "abcçdefghıijklmnoöpqrsştuüvwxyz" # alfabe kullanılacak
alfabe = "abcçdefghıijklmnoöpqrsştuüvwxyz" # alfabe kullanılacak
mesaj = input("Mesajınızı giriniz: ") # Şifrelenecek mesaj
key = "çşöüğabcıdefghjklmnoöpqrsıtuüvwxyz" # Anahtar oluşturma
key2 = "fghıjklmnoöpqrsştuüvwxyzabcçdef" # Anahtar oluşturma
key3 = "vwxyzabcçdefghıijklmnoöpqrsştuü" # Anahtar oluşturma
key4 = "tuüvwxyzabcçdefghıijklmnoöpqrsş" # Anahtar oluşturma
key5 = "ştuüvwxyzabcçdefghıijklmnoöpqrs" # Anahtar oluşturma
key6 = "rsştuüvwxyzabcçdefghıijklmnoöpqr" # Anahtar oluşturma
key7 = "qrştuüvwxyzabcçdefghıijklmnoöpqs" # Anahtar oluşturma
key8 = "pqrsştuüvwxyzabcçdefghıijklmnoöp" # Anahtar oluşturma
key9 = "opqrştuüvwxyzabcçdefghıijklmnoöp" # Anahtar oluşturma
key10 = "nopqrştuüvwxyzabcçdefghıijklmnoö" # Anahtar oluşturma


keys = input("Key Seçiniz(Örnek key4) : ")

if keys == "key":
    key = key
elif keys == "key2":
    key = key2
elif keys == "key3":
    key = key3
elif keys == "key4":
    key = key4
elif keys == "key5":
    key = key5
elif keys == "key6":
    key = key6
elif keys == "key7":
    key = key7
elif keys == "key8":
    key = key8
elif keys == "key9":
    key = key9
elif keys == "key10":
    key = key10
else:
    print("Key bulunamadı")

try:
    try:
        print("Şifrelenmiş mesaj: ", end="") # Şifrelenmiş mesajı ekrana yazdırmak için
        for i in mesaj: # Mesajın her bir karakterini döngüye sokarak
            if i in alfabe: # Eğer karakter alfabe içindeyse
                indis = alfabe.index(i) # Karakterin indisini bulma
                print(key[indis], end="") # Anahtarın indisindeki karakteri ekrana yazdırma
            else: # Eğer karakter alfabe içinde değilse
                print(i, end="") # Karakteri ekrana yazdırma
        print("") # Ekrana bir boşluk bırakma
        print("Anahtar: ", (key)) # Anahtarı ekrana yazdırma
    except: # Hata oluşursa
        print("Hata oluştu!") # Hata mesajını ekrana yazdırma
except KeyboardInterrupt:
    print("\nProgramdan çıkılıyor...")
 