# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('flight_log')

print("")
print("-=<   Welcome in our Flight Club's Electronic Flight Logger   >=-\n")
print("   Hope you find this program useful addition to your Logbook!\n")

def menu():
    """
    Main menu with all the options currently implemented
    """

    print("Please choose one of the following options:\n")
    print("[1] Option 1 - Instructions")
    print("[2] Option 2 - Last engine maintenence time")
    print("[3] Option 2 - Next engine maintenence time")
    print("[4] Option 3 - Log a flight")
    print("[0] Exit")

def instructions():
    """
    Instruction submenu witha a few lines how to use the program for Option 1
    """
    print("")
    print("You can choose the desired option from the main menu.") 
    print("If you choose 0, the program will exit!")

def last_maint():
    """
    Getting the last maintenance info from the relevant sheet from Google Sheets for Option 2
    """

    maintenance=[]
    maintenance=SHEET.worksheet("maintenance").get_all_values()
    maint_row=maintenance[-1]
    print("")
    print(f"The last Engine maintenance has been done at {(maint_row[0])} hr Tacho-time.")

def next_maint():
    """
    Getting the next maintenance info from the relevant sheet from Google Sheets for Option 3
    """
    maintenance=[]
    maintenance=SHEET.worksheet("maintenance").get_all_values()
    maint_row=maintenance[-1]
    print("")
    print(f"Next engine check due at {(maint_row[1])} hr Tacho-time.")

menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        #option 1 - instructions
        instructions()
    elif option == 2:
        #option 2 - last Engine maintenance time
        last_maint()
    elif option == 3:
        #option 3 - next Engine maintenance due
        next_maint()
    elif option == 4:
        #option 4 - log a flight
        print("Option 4 has been called")
    else:
        print("")
        print("Invalid option.")

    print()
    menu()
    option = int(input("Entert your option: "))

print("Thanks for using this program!")

