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
# +   *            ||: . ||:.     . .   .  ,   ||:   |               *
#         *       ||:   ||:  ,     +       .  ||: , |      +
#  *              ||:   ||:.     +++++      . ||:   |         *
#     +           ||:   ||.     +++++++  .    ||: . |    +
#           +     ||: . ||: ,   +++++++ .  .  ||:   |             +
#                 ||: . ||: ,   +++++++ .  .  ||:   |        *
#                 ||: . ||: ,   +++++++ .  .  ||:   |
#       _________   _____________    ______   ____  ___    ________
#     / ____/   | / ___/_  __/ /   / ____/  / __ \/   |  /  _/ __ \
#    / /   / /| | \__ \ / / / /   / __/    / /_/ / /| |  / // / / /
#   / /___/ ___ |___/ // / / /___/ /___   / _, _/ ___ |_/ // /_/ /
#   \____/_/  |_/____//_/ /_____/_____/  /_/ |_/_/  |_/___/_____/
# ----------------------------------------------------------------------------#
from sys import exit

print("Welcome traveler! You have entered the Magical Adventure Game\n")
print("To continue, please enter your name\n")  # Asks user for a name


def get_info():  # Gets users name and verifies age

    name = input("> ")  # Obtains users name

    print("\nHello " + name + ", Please enter your age:\n ")  # Asks for age

    age = int(input("> "))  # Obtains users age

    if age >= 18:  # Verifies user is 18 or over
        return("\nOkay, your old enough, welcome to a world of fun!\n")

    elif age < 18:  # Exits if user is under 18
        print("Sorry, you dont seem to be of age")
        exit(0)

print(get_info())  # Prints the get_info() function


def final_room(end):  # Last room

    print("\nYou enter the room and find a princess tied up to a bed naked\n")
    print("1. Rape the bitch, steal anything you can carry and leg it\n")
    print("""2. Untie her and cover her with the bed sheet for warmth, then
jump out of the window with her and deploy your parachute for a romantic
skydive\n""")

    choice = ""
    while choice != 1:  # Loops back to this point if input is not 1 or 2
        choice = int(input("What do you do? > "))  # Gets users choice

        if choice == 1:  # Moves to congratulations(gratz) function
            congratulations("""
\nYou attempt to penetrate her but due to your
excessive drinking, you are unable to rise to the occasion. You leave her tied
up to the bed, steal as much as you can and make away with your loot to live a
rich and happy life""")

        elif choice == 2:  # Moves to dead(niceone) function
            print("""
\nYou dive out of the window with the distressed dame and
realise you dont have a parachute because who the fuck takes a parachute on a
castle raid\n""")
            dead("You Both fall and splat against the rocks below\n")

        else:  # Prints message if 1 or 2 is not inputted
            print("Pick a number asshole")


def spider_room():  # Room with spiders

    print("\nYou enter the room and find it filled with man-eating spiders\n")

    print("1. scream like the lil bitch you are and run\n")
    print("2. spray the pricks with petrol and light the place up\n")

    choice = ""
    while choice != 1:  # Loops back to this point if input is not 1 or 2
        choice = int(input("What do you do? > "))  # Gets users choice

        if choice == 1:  # Moves to dead(niceone) function
            dead("""
\nThe spiders are very fast and you're not exactly in the best shape,
they consume you completely, leaving nothing but bone\n""")

        elif choice == 2:  # Moves to final_room(end) function
            final_room("""
\nThe eight legged arachnids scream as they burn whilst you
laugh like a maniac.""")

        else:  # Prints message if 1 or 2 is not inputted
            print("Pick a number asshole")


def congratulations(gratz):  # Message for the end of the game
    print(gratz, """

\nThats it my young adventurer, you have completed the quest,
good job! Now go enjoy your spoils and live out the rest of your life""")
    exit(0)


def dead(niceone):  # Displays message when user dies
    print(niceone, " \nur ded now")
    exit(0)


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
