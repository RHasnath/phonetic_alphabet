#Phonetic Alphabet
#A simple script to help remember phonetic alphabet both in English and Spanish.
#Author: Rezaul Hasnath

import time

print("Welcome to Phonetic Alphabet, v1.0")
print("Author: Rezaul Hasnath (rhasnath@contecnow.com / rez@live.co.uk). Source code available on Github.")
print ("-----------------------------------")
en_dict = {"A":"Alfa", "B":"Bravo", "C":"Charlie", "D":"Delta", "E":"Echo", "F":"Frank", "G":"George", "H":"Hotel", "I":"India", "J":"John", "K":"Kilo", "L":"Lima", "M":"Mike", "N":"November", "O":"Oscar", "P":"Paul", "Q":"Queen", "R":"Romeo", "S":"Sydney", "T":"Tom", "U":"Union", "V":"Victor", "W":"William", "X":"X-ray", "Y":"Yankee", "Z":"Zebra", " ":"SPACE",
 "1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9", ",":"COMA", ".":"FULLSTOP", "@":"@(at)" }
es_dict = {"A":"Antonio", "B":"Barcelona", "C":"Carmen", "D":"Dinamarca", "E":"España", "F":"Francia", "G":"Granada", "H":"Huelva", "I":"Italia", "J":"Jueves", "K":"Kilo", "L":"Lorenzo", "M":"Madrid", "N":"Navarra", "O":"Oviedo", "P":"Paris", "Q":"Queso", "R":"Roma", "S":"Sevilla", "T":"Toledo", "U":"Uruguay", "V":"Valencia", "W":"Washington", "X":"Ximena", "Y":"Yegua", "Z":"Zaragoza", " ":"SPACIO", 
"1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9", ",":"COMA", ".":"PUNTO", "@":"@(arroba)"   }
while True:
    
    selection = input ("Select a language (1.English 2.Español): ")
    
    if selection == "1":
        eng_text = input ("\n[English] Enter your phrase: ")
        eng_text = eng_text.upper()
        eng_list = (eng_text)
        for i in eng_list:
            print (en_dict.get(i), end=" ")
        another = ""    
        another = input ("\n\nTry another one (y/n): ")
        if another == "y":
            continue
        else:
            print ("Good-bye!")
            time.sleep(1) 
            break

    if selection == "2":
        esp_text = input ("\n[Español] Entra la frase: ")
        esp_text = esp_text.upper()
        esp_list = (esp_text)
        for i in esp_list:
        
            print (es_dict.get(i), end=" ")
            
        another2 = input ("\n\nQuieres probar otro:(s/n): ")
        if another2 == "s":
            continue
        else:
            print ("Adiós!")
            time.sleep(1) 
            break

    if selection == "3":
        print ("Bye-bye!")
        time.sleep(1) 
        break

    else:
        print ("Select a valid option. Type 3 for exit")
        continue