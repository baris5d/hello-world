from time import sleep
import os

#hello = ["H","e","l","l","o",",","W","o","r","l","d"] #Aranacak Kelime {Berat Başkan'dan Trick'ler}
hello = "Hello, World"
hello.split()
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",",",".","+","-","_","="," "] #Alfabe

result = '' 
i = 0
for x in hello:
    bulundu = False
    while(bulundu==False):
        sleep(0.02)
        print(result + alphabet[i] , end="\r") 
        if(ord(alphabet[i])==ord(x)):
            bulundu = True
            result = result + alphabet[i]
            i = 0 
            break
        i = i + 1
print(result, end="\r") 