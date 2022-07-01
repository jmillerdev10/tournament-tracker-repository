num_participants = int(0)
tourney_participants = {}
# participant_name = ''

def MenuSelection(option):
    # print("You selected option " + option + "\n")
    if option == '1':
        global num_participants
        while num_participants > 0:
            print("Participant Sign Up\n====================")
            participant_name = input("Participant Name: ")
            desired_slot = input("Desired starting slot #: ")
            tourney_participants.update({desired_slot:participant_name})
            print(tourney_participants)
            # global num_participants
            num_participants -= 1
        ParticipantMenu(num_participants)

    # elif option == '2':
    #     WelcomeScreen()
    elif option == '3':
        print("View Participants\n==================")
    # elif option == '4':
    #     # do something 
    elif option == '5':
        exit()
    else:
        print("You entered an invalid option. Type a number between 1 and 5, then press Enter.")


def WelcomeScreen():
    print("Welcome to Tournaments R Us")
    print("============================")
    global num_participants
    num_participants = int(input("Enter the number of participants: "))
    print("There are " + str(num_participants) + " participant spots ready for sign-ups\n")
    ParticipantMenu(num_participants)
    return num_participants


def ParticipantMenu(headcount):    
    print("There are " + str(headcount) + " participant spots remaining for sign-ups\n")
    print("Participant Menu")
    print("=================")
    print("1. Sign Up \n2. Cancel Sign Up \n3. View Participants \n4. Save changes \n5. Exit")
    print("\n(Type the number and press enter to navigate)")

    menu_selection = input("What would you like to do? ")
    # print("menu_selection was: " + str(menu_selection))
    MenuSelection(menu_selection)

WelcomeScreen()

# print("\n")
# print("There are " + str(num_participants) + " participant spots ready for sign-ups")

# print("\n")
# print("Participant Menu")
# print("=================")
# print("1. Sign Up \n2. Cancel Sign Up \n3. View Participants \n4. Save changes \n5. Exit")
# print("\n(Type the number and press enter to navigate)")

# menu_selection = input("What would you like to do? ")
# print("menu_selection was: " + str(menu_selection))
# MenuSelection(menu_selection)

# if menu_selection == 1:
#         print("Participant Sign Up\n====================")
#         participant_name
#         participant_name = input("Participant Name: ")
#         desired_slot = input("Desired starting slot #:")

