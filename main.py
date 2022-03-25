import time, pyfiglet
from search_skin import search

options = {
    "twd": "Teeworlds data",
    "ddnet": "DDNet skin library"
}

def main():
    ascii_banner = pyfiglet.figlet_format("Tyrone skin fetcher")

    print(ascii_banner)
    # time.sleep(1)

    print("starting up please wait")
    # time.sleep(5)

    print("Hey thanks for using Tyrones Teeworlds skin grabber! Please choose from one of the following options below:")
    # time.sleep(1)

    print("Here are the lists of the current websites available to search for skins on")
    # time.sleep(0.5)

    print(options)
    reply = input("What website do you wish to search for skins on? ").strip()

    if (reply == "twd" or reply == "teeworlds data"):
        search("https://skins.tw/search/")
    elif (reply == "ddnet" or reply == "ddnet skin libary"):
        search("https://ddnet.tw/skins/index.php?search=")
    else:
        print("Sorry that was not a option!")

if __name__ == '__main__':
    main()
