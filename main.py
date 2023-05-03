#Imports
import os
from time import sleep as wait
import math

#Config
coins = 0
inf = float('inf')
workers = 1
adworkers = 0
garrett = 0
ryan = 0
ayden = 0
Doubleclick = 0
Golden_garrett = 0
resets = 0
mega_resets = 0 

worker_cost = 100
adworker_cost = 200
garret_cost =  500
ryan_cost = 5000
ayden_cost = 1000000000000000
Golden_garrett_cost = 50000
Doubleclick_cost = 5000
reset_cost = 1000000
mega_reset_cost = 4

shown_buy = False
clickset = True
first_buy = True
doubleclick_bought = False
Golden_garrett_bought = False
cheats_enabled = False
anticheat_disabled = False

show_reset = False
first_reset = False

show_mega_reset = False
first_mega_reset = False

def clear():
  os.system('clear')

#Game code
while True:
  clear()
  print("Stats")
  print("Clicks: {}".format(coins))
  if shown_buy:
    print("Clickers: {}".format(workers))
  if shown_buy:
    print("Adclickers: {}".format(adworkers))
  if shown_buy:
    print("Garrets: {}".format(garrett))
  if shown_buy:
    print("Ryan: {}".format(ryan))
  if shown_buy:
    print("Aydens: {}".format(ayden))
  if doubleclick_bought == True:
    print("DoubleClick: {}".format(Doubleclick))
  if Golden_garrett_bought == True:
    print("Golden Garrett: {}".format(Golden_garrett))
  if show_reset:
    print("Resets: {}".format(resets))
  if show_mega_reset:
    print("Mega Resets: {}".format(mega_resets))

  if coins == 0:
    print("Type '/h' for help menu, or press ENTER to gain coins.")
    
  if coins >= worker_cost and shown_buy == False:
    clear()
    print("You now have {} coins!\nYou can now buy more workers to increase your productivity.\nTo open your buy menu run the command '/b'".format(coins))
    print("Closing in 5 seconds")
    wait(5)
    input("[ENTER]")
    shown_buy = True
    clear()
      
  if coins >= reset_cost and show_reset == False:
     clear()
     print("You now have {} coins!\nYou can now Reset\nThis will double your output, but will take away EVERYTHING!\nTo reset type '/r'".format(coins))
     print("Closing in 5 seconds")
     wait(5) 
     input("[ENTER]")
     show_reset = True
     clear()
  
  if resets >= mega_reset_cost and show_mega_reset == False:
    clear()
    print("You have {} resets!\nYou can now MEGA RESET\nThis will double the amount of resets you get\nBut takes away all things under it\nTo mega reset type /mr".format(resets))
    print("Closing in 5 seconds")
    wait(5)
    input("[ENTER]")
    show_mega_reset = True
    clear()
    
  run_arg = input("? ")
  if run_arg == "/h":
    clear()
    print("https://trello.com/b/aQLk1j0k/clicker-game")
    input("Press [ENTER] to continue")
  elif run_arg == "/b" and shown_buy:
    ref = ""
    while True:
        clear()
        print("Welcome to the SHOP.\nPlease type in the id of the product you'd like to purchase!")
        if ref == "close":
            break
        print("Clickers:")
        print("[id: 1] Clicker ({} coins)".format(worker_cost))
        print("[id: 2] Adclicker({} coins)".format(adworker_cost))
        print("[id: 3] Garrett({} coins)".format(garret_cost))
        print("[id: 4] Ryan({} coins)".format(ryan_cost))
        print("[id: 5] Ayden({} coins)".format(ayden_cost))
        print("Upgrades:")
        print("[id: 6] DoubleClick(1 time use)({} coins)".format(Doubleclick_cost))
        print("[id: 7] Golden Garrett(1 time use)({} coins)".format(Golden_garrett_cost))
        if first_buy:
            print("Type '/e' to exit menu.")
            first_buy = False
        selected_id = input("id: ")
        if selected_id == "/e":
            break
        elif selected_id == "1" and coins >= worker_cost:
            while True:
                clear()
                print("How many Clickers would you like to purchase?")
                number = input("# ")
                if number == "max":
                    number = math.floor(coins / worker_cost)
                else:
                    try:
                        number = int(number)
                        if number <= 0:
                          print("Number cannot be negative.")
                          input("Press [ENTER] to try again.")
                    except ValueError:  # fixed exception type
                        print("That isn't a number!")
                        input("Press [ENTER] to try again.")
                        continue  # added to skip remaining code in loop
                if number * worker_cost <= coins:
                    coins -= number * worker_cost
                    workers += number
                    ref = "close"
                else:
                    print("Not enough coins.")
                    input("Press [ENTER] to continue.")
                    ref = ""
                break
        elif selected_id == "2" and coins >= adworker_cost:
            while True:
                clear()
                print("How many Adclickers would you like to purchase?")
                number = input("# ")
                if number == "max":
                    number = math.floor(coins / adworker_cost)
                else:
                    try:
                        number = int(number)
                        if number <= 0:
                          print("Number cannot be negative.")
                          input("Press [ENTER] to try again.")
                    except ValueError:
                        print("That isn't a number!")
                        input("Press [ENTER] to try again.")
                        continue
                if number * adworker_cost <= coins:
                    coins -= number * adworker_cost
                    adworkers += number
                    ref = "close"
                else:
                    print("Not enough coins.")
                    input("Press [ENTER] to continue.")
                    ref = ""
                break
        elif selected_id == "6" and coins >= Doubleclick_cost:
          while True:
            if Doubleclick == 1:
              print("You already have already bought Doubleclick.")
              input("Press [ENTER] to continue.")
              ref = "close"
              break
            else:
             clear()
             print("Would you like to buy DoubleClick? this is a one time purchase.\nY/N")
             number = input("# ")
             if number == "Y" or "y":
               coins -= Doubleclick_cost
               Doubleclick += 1
               doubleclick_bought = True
               ref = "close"
               break
             if number == "N" or "n":
               print("Purchase cancelled.")
               input("Press [ENTER] to continue.")
               ref = "close"
               break
               if coins < 5000:
                    print("Not enough coins.")
                    input("Press [ENTER] to continue.")
                    ref = "close"
                    break
        elif selected_id == "5" and coins >= ayden_cost:
            while True:
                clear()
                print("How many Aydens would you like to purchase?")
                number = input("# ")
                if number == "max":
                    number = math.floor(coins / adworker_cost)
                else:
                    try:
                        number = int(number)
                        if number <= 0:
                          print("Number cannot be negative.")
                          input("Press [ENTER] to try again.")
                    except ValueError:
                        print("That isn't a number!")
                        input("Press [ENTER] to try again.")
                        continue
                if number * ayden_cost <= coins:
                    coins -= number * ayden_cost
                    ayden += number
                    ref = "close"
                else:
                    print("Not enough coins.")
                    input("Press [ENTER] to continue.")
                    ref = ""
                break
        elif selected_id == "3" and coins >= garret_cost:
            while True:
                clear()
                print("How many Garretts would you like to purchase?")
                number = input("# ")
                if number == "max":
                    number = math.floor(coins / garret_cost)
                else:
                    try:
                        number = int(number)
                        if number <= 0:
                          print("Number cannot be negative.")
                          input("Press [ENTER] to try again.")
                    except ValueError:
                        print("That isn't a number!")
                        input("Press [ENTER] to try again.")
                        continue
                if number * garret_cost <= coins:
                    coins -= number * garret_cost
                    garrett += number
                    ref = "close"
                else:
                    print("Not enough coins.")
                    input("Press [ENTER] to continue.")
                    ref = ""
                break
        elif selected_id == "4" and coins >= ryan_cost:
            while True:
                clear()
                print("How many Ryans would you like to purchase?")
                number = input("# ")
                if number == "max":
                    number = math.floor(coins / worker_cost)
                else:
                    try:
                        number = int(number)
                        if number <= 0:
                          print("Number cannot be negative.")
                          input("Press [ENTER] to try again.")
                    except ValueError:  # fixed exception type
                        print("That isn't a number!")
                        input("Press [ENTER] to try again.")
                        continue  # added to skip remaining code in loop
                if number * ryan_cost <= coins:
                    coins -= number * ryan_cost
                    ryan += number
                    ref = "close"
                else:
                    print("Not enough coins.")
                    input("Press [ENTER] to continue.")
                    ref = ""
                break
        elif selected_id == "7" and coins >= Golden_garrett_cost:
          while True:
            if Golden_garrett == 1:
              print("You already have already bought a Golden Garrett.")
              input("Press [ENTER] to continue.")
              ref = "close"
              break
            else:
             clear()
             print("Would you like to buy a Golden Garrett? this is a one time purchase.\nY/N")
             number = input("# ")
             if number == "Y" or "y":
               coins -= Golden_garrett_cost
               Golden_garrett += 1
               Golden_garrett_bought = True
               ref = "close"
               break
        else:
            print("Invalid selection or not enough coins.")
            input("Press [ENTER] to continue.")
            ref = ""  
  elif run_arg == "/r" and show_reset:
    clear()
    if coins < reset_cost:
      print("You are much to weak to reset!\nCome back when you are wealthy!")
      input("[ENTER] to continue.")
    elif coins >= reset_cost:
      print("You meet the requirments to reset.\nAre you sure\n(YOU WILL LOSE EVERYTHING)")
      sure = input("y/n ")
      if sure == "y":
        print("Wonderful!\nI you will now recieve {} coins per worker!".format(resets+1))
        coins = 0
        workers = 1
        adworkers = 0
        Doubleclick = 0
        garrett = 0
        Golden_garrett = 0
        ayden = 0
        doubleclick_bought = False
        resets += 1
        reset_cost *= 2
      else:
        clear()
        print("I understand.")
  elif run_arg == "/mr" and show_mega_reset:
    clear()
    if resets < mega_resets:
      print("You are not wealthy enough to gain a mega reset!\nYou need {} resets to mega reset!".format(mega_reset_cost))
    else:
      print("You meet the requirements to mega reset.\nAre you sure?(YOU WILL LOSE 4 RESETS AND EVERYTHING ELSE")
      sure = input("y/n ")
      if sure == "y":
        print("Wonderful!\nI you will now recieve {} coins per worker!".format(mega_resets+5))
        coins = 0
        workers = 1
        adworkers = 0
        Doubleclick = 0
        garrett = 0
        Golden_garrett = 0
        ayden = 0
        doubleclick_bought = False
        resets -= 4
        mega_resets += 1
        mega_reset_cost *= 2
      else:
        clear()
        print("I understand.")
      
      pass
  elif run_arg == "":
   aval = adworkers * (Doubleclick * (resets + 1) + 4)
   val = workers * (Doubleclick * (resets + 1) + 1)
   ayval = ayden * (Doubleclick * (resets + 1) + 1000000000)
   garval = garrett * (Doubleclick * (resets +1) * (Golden_garrett + 1) + 5)
   ryval = ryan * (Doubleclick * (resets +1) + 10)
   total_val = val + aval + ayval + garval + ryval
   if doubleclick_bought:
      total_val *= 2
   if mega_resets >= 1:
      total_val *= 5
   coins += total_val
   
    
  if run_arg == "/ec":
      print("cheats enabled")
      cheats_enabled = True
      input("Press [Enter] to continue")

  if run_arg == "/da":
      print("do you want to disable the antichear?")
      sure = input("Y/N ")
      if sure == "Y" or "y":
        anticheat_disabled = True
      else:
        print("anticheat not disabled")   
  if run_arg == "/$":
      if cheats_enabled == False:
        print("commands not enabled")
        input("Press [ENTER] to continue")
      if cheats_enabled and anticheat_disabled == True:
       coins += 10000000
       print("+10000000 coins added")
       input("Press [ENTER] to continue")

  if run_arg == "/$$":
      if cheats_enabled == False:
        print("commands not enabled")
        input("press [ENTER] to continue")
      if cheats_enabled and anticheat_disabled == True:
       coins += inf
       print("+inf coins added")
       input("Press [ENTER] to continue")

  if run_arg == "/rc":
      if anticheat_disabled == False:
       if cheats_enabled == False:
        print("commands not enabled")
        input("Press [ENTER] to continue")
      if cheats_enabled and anticheat_disabled == True:
       coins = 0 
       print("coins reset")
       print("press [ENTER] to continue")

  if run_arg == "/sc":
    new_coins = input("Coins: ")
    coins = int(new_coins)
    print("Coins set to {}".format(coins))
  if run_arg == "/sw":
    new_workers = input("Clickers: ")
    workers = int(new_workers)
  if run_arg == "/saw":
    new_adworkers = input("Adclickers: ")
    adworkers = int(new_workers)
  if run_arg == "/sdc":
    new_dc = input("Doubleclick: ")
    Doubleclick = int(new_dc)
  if run_arg == "/sr":
    new_resets = input("Resets: ")
    resets = int(new_resets)
    