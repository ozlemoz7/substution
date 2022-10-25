import random
import optparse
import json
from tkinter import *

alfabe = "abcçdefghıijklmnoöpqrsştuüvwxyz" # alfabe kullanılacak
mesaj = input("Mesajınızı giriniz: ") # Şifrelenecek mesaj
try:
    try:
        key = random.choices(alfabe, k=len(alfabe)) # Anahtar oluşturma
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