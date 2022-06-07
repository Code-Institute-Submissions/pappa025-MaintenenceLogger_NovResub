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

flights = SHEET.worksheet('flights')

print("-=<   Welcome in our Flight Club's Electronic Flight Logger   >=-\n")
print("   Hope you find this program useful addition to your Logbook!\n")

def menu():
    print("Please choose one of the following options:")
    print("[1] Option 1 - Instructions")
    print("[2] Option 2 - Last engine maintenence time")
    print("[3] Option 3 - Log a flight")
    print("[0] Exit")

def instructions():
    print("")
    print("You can choose the desired option from the main menu.") 
    print("If you choose 0, the program will exit!")

menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        #option 1 - instructions
        instructions()
    elif option == 2:
        #option 2 - last engine maintenecae time
        print("Option 2 has been called")
    elif option == 3:
        #option 3 - log a flight
        print("Option 3 has been called")
    else:
        print("Invalid option.")

    print()
    menu()
    option = int(input("Entert your option: "))

print("Thanks for using this program!")

