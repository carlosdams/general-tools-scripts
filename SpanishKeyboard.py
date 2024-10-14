##!/usr/bin/env python
"""
This program copies Spanish accented letters (i.e. Á, é, ó), ñ, and punctuation like "¿" to the clipboard, there are two uses:
1. Run the program without passing any argument, it copies all the Spanish accented letters uppercase and lowercase, ñ, and the punctuation, 
2. Run the program passing one or multiple of the following characters: aeioun?, it will copy all Spanish accented letters related to the passed letter, uppercase and lowercase
Dependency: it needs pyperclip module installed to access the clipboard, and Windows clipboard history enabled
"""
import os, sys, time
try:
    import pyperclip
except ModuleNotFoundError:
    print("Module pyperclip is not installed")
    os.system("pause")

#Parameter letter currently does not have any use, it might have a use in the future
def get_spanish_letters(letter = None):
    
    #Storing all accented Spanish letters, ñ, and ¿¡
    all_spanish_letters = {"a" : ("Á", "á"), #2
                           "e" : ("É", "é"), #2
                           "i" : ("Í", "í"), #2
                           "o" : ("Ó", "ó"), #2
                           "u" : ("Ú", "Ü", "ú", "ü"), #4
                           "n" : ("Ñ", "ñ"), #2
                           "?" : ("¿","¡")} #2

    #Command line arguments passed:
    if len(sys.argv) == 1: #If no argument is passed, use number 1
        for values in all_spanish_letters.values():
            for item in values:
                pyperclip.copy(item)
                print(item)
                time.sleep(0.3)
        print("Copied all common Spanish letters to clipboard,\nCheck clipboard history with windows key + v")

    elif len(sys.argv) > 1: #If an argument is passed, use number 2
        list_of_letters = []
        for element in sys.argv[1:]:
            letter_fixed = element.lower()
            if len(letter_fixed) > 1: # In case user entered many letters without whitespace
                for char in letter_fixed: 
                    list_of_letters.append(char)
            else:
                list_of_letters.append(letter_fixed)
        for letter in list_of_letters:
            if letter in all_spanish_letters.keys():
                for item in all_spanish_letters[letter]:
                    pyperclip.copy(item)
                    print(item)
                    time.sleep(0.3)
                print(f"Copied the Spanish letters associated with {letter},")
        print(f"Check clipboard history with windows key + v")   
    
    os.system("pause") #To give enough time for user to check the screen

#TODO considering using propmt_toolkit, pyinputplus or click for prompting the user for the letter
get_spanish_letters()