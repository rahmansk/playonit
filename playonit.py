import pywhatkit as k
import datetime

name = """
d8888b. db       .d8b.  db    db  .d88b.  d8b   db d888888b d888888b 
88  `8D 88      d8' `8b `8b  d8' .8P  Y8. 888o  88   `88'   `~~88~~' 
88oodD' 88      88ooo88  `8bd8'  88    88 88V8o 88    88       88    
88~~~   88      88~~~88    88    88    88 88 V8o88    88       88    
88      88booo. 88   88    88    `8b  d8' 88  V888   .88.      88    
88      Y88888P YP   YP    YP     `Y88P'  VP   V8P Y888888P    YP  
"""
print(name)
now = datetime.datetime.now()

print(now.strftime('Current Date: %d-%m-%y'))
print(now.strftime('Time: %H:%M:%S on %A, %B %dth, %Y\n'))

while True:
    music = input("\nSOng !! : ")


    if music == "":
            print("Hey Idiot Type anything Man !!")
            con = input("\nDo You want to try again? [Y/N] : ")
            if not (con[0] == "Y" or con[0] == "y"):
                break

    else:
        print("\nYour Song Is On The Way ;) Enjoy BTW )")
        k.playonyt(music)
        break