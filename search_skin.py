from typing import *
import webbrowser

def search(url: str):
    print("Hey! i see you would like to browse teeworlds data for your next skin!")
    
    teename = input("Please type the name of the skin you would like:")
    reply = input("do you want to open the browser, yes or no? ").strip()
    
    if (reply == "yes"):
        webbrowser.open(url + teename)
    elif (reply == "no"):
        print("Okay, returning to main menu! ")
    else:
        print("sorry that was not an option >:(")
