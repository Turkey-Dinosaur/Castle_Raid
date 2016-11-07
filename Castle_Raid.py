# ------------------------------------------------------------------------------------#
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

# ___  ___            _           _    ___      _                 _
# |  \/  |           (_)         | |  / _ \    | |               | |
# | .  . | __ _  __ _ _  ___ __ _| | / /_\ \ __| |_   _____ _ __ | |_ _   _ _ __ ___
# | |\/| |/ _` |/ _` | |/ __/ _` | | |  _  |/ _` \ \ / / _ \ '_ \| __| | | | '__/ _ \
# | |  | | (_| | (_| | | (_| (_| | | | | | | (_| |\ V /  __/ | | | |_| |_| | | |  __/
# \_|  |_/\__,_|\__, |_|\___\__,_|_| \_| |_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|
#              __/ |      _____
#             |___/      |  __ \
#                        | |  \/ __ _ _ __ ___   ___
#                        | | __ / _` | '_ ` _ \ / _ \
#                        | |_\ \ (_| | | | | | |  __/
#                        \____/\__,_|_| |_| |_|\___|

# ------------------------------------------------------------------------------------#
from sys import exit

print("Welcome traveler! You have entered the Magical Adventure Game\n")
print("To continue, please enter your name\n")

def get_info():  # Gets users name and verifies age

    name = input("> ")  # Obtains users name

    print("\nHello " + name + ", Please enter your age:\n ")

    age = int(input("> "))

    if age >= 18:  # Verifies user is 18 or over
        return("\nOkay, your old enough, welcome to a world of fun!\n")

    elif age < 18:
        print("Sorry, you dont seem to be of age")
        exit(0)

print(get_info())

def final_room(end):

    print("\nYou enter the room and find a princess tied up to a bed naked\n")
    print("1. Rape the bitch, steal anything you can carry and leg it\n")
    print("""2. Untie her and cover her with the bed sheet for warmth, then
jump out of the window with her and deploy your parachute for a romantic
skydive\n""")


    choice = ""
    while choice != 1:
        choice = int(input("What do you do? > "))

        if choice == 1:
            congratulations("""
\nYou attempt to penetrate her but due to your
excessive drinking, you are unable to rise to the occasion. You leave her tied
up to the bed, steal as much as you can and make away with your loot to live a
rich and happy life""")

        elif choice == 2:
            dead("""
\nYou dive out of the window with the distressed dame and
realise you dont have a parachute because who the fuck takes a parachute on a
castle raid\n""")
            dead("You Both fall and splat against the rocks below")

        else:
            print("Pick a number asshole")

def spider_room():

    print("\nYou enter the room and find it filled with man-eating spiders\n")

    print("1. scream like the lil bitch you are and run\n")
    print("2. spray the pricks with petrol and light the place up\n")

    choice = ""
    while choice != 1:
        choice = int(input("What do you do? > "))

        if choice == 1:
            dead("""
\nThe spiders are very fast and you're not exactly in the best shape,
they consume you completely, leaving nothing but bone\n""")

        elif choice == 2:
            final_room("""
\nThe eight legged arachnids scream as they burn whilst you
laugh like a maniac.""")

        else:
            print("Pick a number asshole")

def congratulations(gratz):
    print(gratz, """

\nThats it my young adventurer, you have completed the quest,
good job! Now go enjoy your spoils and live out the rest of your life""")
    exit(0)

def dead(niceone):  # Dead function
    print(niceone, " \nur ded now")
    exit(0)

def start():
    print("\nYou approach the castle and wonder how you will get in\n")
    print("""After an hour of staring at the castle you decide the only way in
is to either:\n""")

    print("1. Shout and hope someone drops the draw bridge")
    print("2. Find an alternative route into the castle\n")

    choice = ""
    while choice != 1:
        choice = int(input("What do you do? > "))

        if choice == 1:
            print("""
\nObviously no one lets you in you idiot, your attacking the
fucking castle, Try again....""")
            start()

        elif choice == 2:
            spider_room()

        else:
            print("pick a number asshole")

start()
