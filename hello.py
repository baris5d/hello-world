from time import sleep
import os

hello = ["H","e","l","l","o",",","W","o","r","l","d"] #Aranacak Kelime

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",",",".","+","-","_","="] #Alfabe

result = '' # oluşan kelimeler
hexresult = '' # oluşan kelimelerin 0-1 cinsinden değeri
for x in hello: # her harf için ara
    for y in alphabet: # alfabeyi gez
        print(hexresult , end="\r") #oluşan anlık değeri ekrana bas
        #print(result+y, end="\r")
        if(ord(y)==ord(x)): # elde edilen değer doğruysa 
            hexresult = hexresult + str(ord(y)%2) # hex kodunu al
            result = result + y # oluşan değeri ekle
            break #for y döngüsünü kır
        print(hexresult + str(ord(y)%2), end="\r") # 0 - 1 değeri ekrana bas    
        sleep(0.05) # birazcık yavaşla hızlı hızlı yapıyon bişi anlamıyoz
print("I Found it!") # ehehueheuh buldu 
sleep(1) # şşş bekle biraz
print(result, end="\r") #Sonuç!
