from typing import *
import webbrowser

def search(url: str):
    print("Cool! lets get this skin for you!")
    
    teename = input("Please type the name of the skin you would like:")
    reply = input("do you want to open the browser, yes or no? ").strip()
    
    if (reply == "yes"):
        webbrowser.open(url + teename)
    elif (reply == "no"):
        print("Okay, returning to main menu! ")
    else:
        print("sorry that was not an option >:(")

def all():
    print("Okay i will search all avaiable websites for you!")
    teename = input("Please type the name of the skin you would like:")
    reply = input("do you want to open the browser, yes or no? ").strip()
    
    if (reply == "yes"):
        webbrowser.open("https://skins.tw/search/" + teename)
        webbrowser.open("https://ddnet.tw/skins/index.php?search=" + teename)
    elif (reply == "no"):
        print("Okay, returning to main menu! ")
    else:
        print("sorry that was not an option >:(")