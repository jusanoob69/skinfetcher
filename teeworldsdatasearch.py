#imported modules
import webbrowser


def search():
    print("Hey! i see you would like to browse teeworlds data for your next skin!")
    teename = input("Please type the name of the skin you would like:")
     
    reply = input("do you want to open the browser, yes or no? ").strip()
    
    if (reply == "yes"):
        webbrowser.open("https://skins.tw/search/"+teename)

    if (reply == "no"):
        print("Okay, returning to main menu! ").strip()
        import main
        main()
        return
    else:
        print("sorry that was not an option >:(")