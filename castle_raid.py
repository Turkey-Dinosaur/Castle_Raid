# ----------------------------------------------------------------------------#
#
#    *                             |>>>                    +
# +          *                      |                   *       +
#                    |>>>      _  _|_  _   *     |>>>
#           *        |        |;| |;| |;|        |                 *
#     +          _  _|_  _    \\.    .  /    _  _|_  _       +
# *             |;|_|;|_|;|    \\: +   /    |;|_|;|_|;|
#               \\..      /    ||:+++. |    \\.    .  /           *
#      +         \\.  ,  /     ||:+++  |     \\:  .  /
#                 ||:+  |_   _ ||_ . _ | _   _||:+  |       *
#          *      ||+++.|||_|;|_|;|_|;|_|;|_|;||+++ |          +
#                 ||+++ ||.    .     .      . ||+++.|   *
# +  *            ||: . ||:.     . .   .  ,   ||:   |               *
#         *       ||:   ||:  ,     +       .  ||: , |      +
#  *              ||:   ||:.     +++++      . ||:   |         *
#     +           ||:   ||.     +++++++  .    ||: . |    +
#           +     ||: . ||: ,   +++++++ .  .  ||:   |             +
#                 ||: . ||: ,   +++++++ .  .  ||:   |        *
#                 ||: . ||: ,   +++++++ .  .  ||:   |
#      _________   _____________    ______   ____  ___    ________
#     / ____/   | / ___/_  __/ /   / ____/  / __ \/   |  /  _/ __ \
#    / /   / /| | \__ \ / / / /   / __/    / /_/ / /| |  / // / / /
#   / /___/ ___ |___/ // / / /___/ /___   / _, _/ ___ |_/ // /_/ /
#   \____/_/  |_/____//_/ /_____/_____/  /_/ |_/_/  |_/___/_____/
# ----------------------------------------------------------------------------#
from sys import exit  # Imports exit from sys
import random  # Import the random module

print("Welcome traveler! You have entered the Magical Adventure Game\n")
print("To continue, please enter your name\n")  # Asks user for a name

def get_info():  # Gets users name and verifies age

    name = input("> ")  # Obtains users name

    print("\nHello " + name.title() + ", Please enter your age:\n ")  # Asks for age
    age = int(input("> "))  # Obtains users age

    if age >= 18:  # Verifies user is 18 or over
        return("\nOkay, your old enough, welcome to a world of fun!\n")

    elif age < 18:  # Exits if user is under 18
        print("Sorry, you dont seem to be of age")
        exit(0)

print(get_info())  # Prints the get_info() function


def final_room():  # Last room

    print("\nYou enter the room to find it filled with treasure and a princess tied up to a bed and think of only 2 options:\n")
    print("1. Rape the bitch, steal as much as you can carry and get out\n")
    print("2. Untie her, and escape together\n")

    choice = ""
    
    while choice != 1:  # Loops back to this point if input is not 1 or 2

      choice = int(input("What do you do? > "))  # Gets users choice

      if choice == 1:  # Moves to dragon_without_princess() function
          print("""\nYou attempt to penetrate her but due to your past excessive drinking, you are unable to rise to the occasion. This angers you greatly. You leave her tied up to the bed, draw the kings sword and pierce her heart. \"Leave no witnesses\" you mutter. You fill your pockets with as much treasure as possible and create a rope from the blood stained bed sheet and curtains to make a hasty escape out of the window\n""")
          dragon_without_princess()

      elif choice == 2:  # Moves to dragon_with_princess() function
        print("""\nYou tie the bed sheets and curtains together to make a sturdy rope. You tie one end to the bed frame and throw the other end out of the window. The princess continually thanks you and mounts your back as you climb out of the window and down the rope\n""")
        print("""you get to the end of the rope and land safely on the ground. As your about to make your departure, the dragon that has been tormenting the locals appears and takes a keen interest in you and the princess. You mutter...\"As if my day wasnt hard enough\"\n""")
        dragon_with_princess()

      else:  # Prints message if 1 or 2 is not inputted
        print("Pick a number asshole")

def dragon_with_princess():
  
  print("""\"Stand back m'lady!\", you shout as you draw your sword, ready to battle the fierce beast. The dragon lets out a loud roar and a plume of fire into the sky as it lands in front of you. You narrowly escape the slash of the dragons razor sharp claws, spotting a chink in the beasts armour as you recover.\n""")
  print("""You dive towards the dragon thrusting your sword directly into it's only weak spot as it falls to the ground.""")
  print("""\"My hero, My hero!\", the princess shouts. You mount your steed along with the princess and ride off into the distance to live out the rest of your days in peace""")
  congratulations()

def dragon_without_princess():

  print("""you get to the end of the rope and land safely on the ground. As your about to make your departure, the dragon that has been tormenting the locals appears and takes a keen interest in you. You mutter...\"As if my day wasnt hard enough\"\n""")
  print("\"It's fabled that the dragon has a small chink in its scaley armour, if im quick enough, i may be able to defeat it\" you think. Do you:\n")
  
  print("1. Wait to see what the dragon does")
  print("2. Attack the dragon with the hope of hitting its weak spot with your sword\n")

  choice = ""
    
  while choice != 1:  # Loops back to this point if input is not 1 or 2

    choice = int(input("What do you do? > "))  # Gets users choice

    if choice == 1:  # Moves to dragon() function
      print("""\nThe dragon approaches fiercely and comes to a stop right in front of you, blasting a huge plume of fire into the sky\n""")
      print("\"Less of the show you overgrown fire cow, prepare to meet your end!\"\n")
      print("The dragon stops in a confused manor, looks down at you and lowers its head\n")
      print("""\"Oh hello there adventurer, i didnt see you there\" says the dragon \"Say, you havent just come from that castle have you?\"\n""")
      print("""You take a step back in awe that this dragon can speak. \"Y...Yes i have, whats it to you beast?\"\n""")
      print("""\"Ive come to take back the treasure that the mad king that lives in there stole from me many moons ago\"\n""")
      print("""\"That gay ass undead mad king in there wont be stealing any more treasure i assure you. When i tried to steal his sword, he tried pulling some magic bullshit on me but i got the better of him\"\n""")
      print("""Excellent!, the dragon roars, \"i shall leave you to your travels, good day adventurer\"\n""")
      print("You and the dragon part ways, to continue on your adventures\n")
      congratulations()
      


    if choice == 2:  # Moves to dragon() function
        print("\nYou run around the dragon searching for its weak spot until it stands up on its hind legs for a brief moment, revealing a chink in it's scales. You slide under the beast and drive your sword directly into the weak spot and scamper from underneath it before you get crushed\n""")
        print("""\"W...Whats happening\" you shout as you notice the dragon start to glow and disintergrate. The light seems to be flowing around you as if you were absorbing it. you look back at the dragon to see all that is left is it's skeleton where it once laid. You hear faint music playing... \"DOVAKIIN!\" bellows from no where, and thus, a new story begins...\n""")
        congratulations()

    else:  # Prints message if 1 or 2 is not inputted
      print("Pick a number asshole")

def kings_room():

  print("You enter the room to find a deceased king sitting on his throne, sword in hand\n")
  print("Upon attempting to take the sword, the king re-animates to slay the thief who dares steal from him\n")
  print("""You hear what seems like the mortal combat theme song playing faintly from no-where. The king waves his hand and an assortment of weapons appear infront of you. \"CHOOSE YOUR WEAPON!\" the king shouts\n""")
  
  print("what weapon do you choose?\n")

  print("1. A used butter knife")
  print("2. A broadsword")
  print("3. A bow and arrows")
  print("4. A dagger\n")
  
  choice = ""

  while choice != 1:  # Loops back to this point if input is not valid

    choice = int(input("What do you do? > "))  # Gets users choice

    if choice == 1:  # Moves to dead() function
      print("""\nYou grab the butter knife and attempt to hold your ground. The king swings his sword towards you, you attempt to defend but the slippery knife is no match for the kings mighty sword""")
      dead()

    elif choice == 2:  # Moves to dead() function
      print("""You attempt to grab the broadsword but under estimate the weight of it and cannot pick it up. The king skewers you like a sheesh kebab""")
      dead()

    elif choice == 3:  # Moves to dead() function
      print("""You grab the bow and arrows but cannot notch an arrow in time. The king slices you into a million pieces""")
      dead()

    elif choice == 4:  # Moves to final_room() function
      print("\nYou quickly grab the dagger, dodge the kings attack and drive it into the kings ribs\n")
      print("""\"HAZAH!\" you shout as the king falls to the ground.... but wait, the king gets back up!\n\"You think i can be defeated so easily peasant?\"\n""")
      print("""Your to far away from the weapons to grab another... you look around the room frantically searching for something to defend yourself with and see something sticking out from the wall. You run to it hoping it can help defeat the king only to find a wall mounted 10 inch thick black dildo. \"YOU GET AWAY FROM THAT THIS INSTANT\" the king bellows whilst running towards you. You desperately start tugging on it in an attempt to pull it off the wall as the king rapidly approaches. With one final mighty tug, you pull the dildo from the wall and spin around, hitting the king over the head, knocking him out cold. You grab his sword and slice his head from his body. You have defeated the mighty undead king!\n""")
      print("You catch your breathe from the weird and unexpected battle and make your way to the door at the back of the room")
      final_room()

    else: # Prints message if invalid choice
      print("choose a weapon dipshit\n")

def spider_room():  # Room with spiders

    print("\nYou enter the room and find it filled with man-eating spiders\n")

    print("1. scream like the lil bitch you are and run\n")
    print("2. spray the pricks with petrol and light the place up\n")

    choice = ""

    while choice != 1:  # Loops back to this point if input is not 1 or 2

        choice = int(input("What do you do? > "))  # Gets users choice

        if choice == 1:  # Moves to dead() function
            print("""
\nThe spiders are very fast and you're not exactly in the best shape,
they consume you completely, leaving nothing but bone\n""")
            dead()

        elif choice == 2:  # Moves to kings_room() function
            print("""
\nThe eight legged arachnids scream as they burn whilst you laugh like a
maniac and run to the next room\n""")
            kings_room()

        else:  # Prints message if 1 or 2 is not inputted
            print("Pick a number asshole")


def congratulations():  # Message for the end of the game
    print("""\nThats it my young adventurer, you have completed the quest.... Until the next one""")
    exit(0)


def dead():  # Displays message when user dies
    print("\nNice one, you died!\n")
    print("Would you like to restart?\n")

    choice = input("> ")

    if choice == "yes" or choice == "y":
        start()

    elif choice == "no" or choice == "n":
        print("Maybe another time then")
        exit(0)

    else:
        print("stop dickin around")


def start():  # First part of the game
    print("\nYou approach the castle and wonder how you will get in\n")
    print("""After an hour of staring at the castle you decide the only way in
is to either:\n""")

    print("1. Shout and hope someone drops the draw bridge")
    print("2. Find an alternative route into the castle\n")

    choice = ""
    while choice != 1:  # Loops back to this point if input is not 1 or 2
        choice = int(input("What do you do? > "))  # Gets users choice

        if choice == 1:  # Loops back to the beginning of the start() function
            print("""
\nObviously no one lets you in you idiot, your attacking the
fucking castle, Try again....""")
            start()

        elif choice == 2:  # Moves to spider_room function
            spider_room()

        else:  # Prints message if 1 or 2 is not inputted
            print("pick a number asshole")

start()