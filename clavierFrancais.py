#!/usr/bin/env python
"""
This program copies French accented letters and cedilla (i.e. À, é, ç) to the clipboard, there are two uses:
1. Run the program without passing any argument, it copies the common French accented letters (e.g. à, é, ç) uppercase and lowercase
2. Run the program passing one or multiple of the following letters: aeiouyc, it will copy all French accented letters related to the passed letter, uppercase and lowercase
Dependency: it needs pyperclip module installed to access the clipboard, and Windows clipboard history enabled
"""
import os, sys, time
try:
    import pyperclip
except ModuleNotFoundError:
    print("Module pyperclip is not installed")
    os.system("pause")

#Parameter letter currently does not have any use, it might have a use in the future
def get_french_letters(letter = None):
    
    #Storing all French accented letters and cedilla
    all_french_letters = {"a" : ("À", "Â", "Æ", "à", "â", "æ"), #6
                          "e" : ("É", "È", "Ê", "Ë", "é", "è", "ê", "ë"), #8
                          "i" : ("Î", "Ï", "î", "ï"), #4
                          "o" : ("Ô", "Œ", "ô", "œ"), #4
                          "u" : ("Ù", "Û", "Ü", "ù", "û", "ü"), #6
                          "y" : ("Ÿ", "ÿ"), #2
                          "c" : ("Ç", "ç")} #2
    
    common_french_letters = {"a" : ("À", "Â", "à", "â"), #4
                             "e" : ("É", "È", "Ê", "é", "è", "ê", "ë"), #7
                             "i" : ("Î", "î", "ï",), #3
                             "o" : ("Ô", "Œ", "ô", "œ"), #4
                             "u" : ("ù", "û", "ü"), #3
                             "y" : ("ÿ"), #1
                             "c" : ("Ç", "ç")} #2

    #Command line arguments passed:
    if len(sys.argv) == 1: #If no argument is passed, use number 1
        for values in common_french_letters.values():
            for item in values:
                pyperclip.copy(item)
                print(item)
                time.sleep(0.3)
        print("Copied all common French letters to clipboard,\nCheck clipboard history with windows key + v")

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
            if letter in all_french_letters.keys():
                for item in all_french_letters[letter]:
                    pyperclip.copy(item)
                    print(item)
                    time.sleep(0.3)
                print(f"Copied the French letters associated with {letter},")
        print(f"Check clipboard history with windows key + v")   
    
    os.system("pause") #To give enough time for user to check the screen

#TODO considering using propmt_toolkit, pyinputplus or click for prompting the user for the letter
get_french_letters()