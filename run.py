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
    print("[3] Option 3 - Next engine maintenence due")
    print("[4] Option 4 - Calculate time left in Engine")
    print("[5] Option 5 - Log a flight")
    print("[0] Exit")

def instructions():
    """
    Instruction submenu with a a few lines how to use the program for Option 1
    """
    print("")
    print("You can choose the desired option from the main menu.") 
    print("If you choose 0, the program will exit!")

maintenance=[]
maintenance=SHEET.worksheet("maintenance").get_all_values()
maint_row=maintenance[-1]

def last_maint():
    """
    Getting the last maintenance info from the relevant sheet from Google Sheets for Option 2
    """
    print("")
    print(f"The last Engine maintenance has been done at {(maint_row[0])} hr Tacho-time.")

def next_maint():
    """
    Getting the next maintenance info from the relevant sheet from Google Sheets for Option 3
    """
    print("")
    print(f"Next engine check due at {(maint_row[1])} hr Tacho-time.")

data = []

def engine_time_left():
    """
    !!!Need to extract all colum of flight times, then subtract from maint row differecnce!!!
    """
    time_left = float(maint_row[1])-float(maint_row[0])
    print(f"Calculating time left in engine: ... {time_left}\n")
    menu()

def log_to_sheet():
    """
    Calculating price of flight out of entered flight time, and ogging the cumulated flight log data back to Google Sheets
    At the End of the Function option takes back to Main Menu
    Last part of the Log a Flight option journey
    """
    print("")
    price = float(data[-1]) * 160
    data.append(price)
    data_worksheet = SHEET.worksheet("flights")
    data_worksheet.append_row(data)
    print(f"If the hourly rate is €160, the cost of this flight was: €{price}\n")
    print("Adding the inputted informations to the electronic Flight Log...\n")    
    print("Thank you to use this program!\n")
    menu()

def flight_time():
    """
    Logging flight time as part of Log a Flight journey
    !!!To be implemented to check if its a right format and go back to main menu if hitting 0
    """
    print("")
    time = input("Flight time in hours (0.3, 1.4, etc..):")
    data.append(time)
    log_to_sheet()

def landings():
    """
    Logging landings as part of Log a Flight journey
    !!!To be implemented to check if its a format, cant be less or more than takeoff and go back to main menu if hitting 0 
    !!!Option to make it together with Takeoffs!
    """
    print("")
    ldgs = input("Number of Landings:")
    data.append(ldgs)
    flight_time()

def takeoffs():
    """
    Logging takeoffs as part of Log a Flight journey
    !!!To be implemented to check if its a format, go back to main menu if hitting 0 
    !!!Option to make it together with Landings!
    """
    print("")
    toffs = input("Number of Takeoffs:")
    data.append(toffs)
    landings()

def registration():
    """
    Logging aircraft registration as part of Log a Flight journey
    Check if its a 3 letters format, go back to main menu if hitting `
    """
    print("")
    while True:
        reg = input("Aircraft registration (3 letters): EI-")
        if reg == "`":
            print("")
            print("Logging process cancelled, back to main menu!\n")

            menu()
        if len(reg) != 3 or not reg.isalpha():
            print("")
            print("Registration should be  three letters Only!\n")
        else:
            data.append(reg.upper())
            takeoffs()
            break

def arrival():
    """
    Logging Arrival Airfield as part of Log a Flight journey
    !!!To be implemented to check if its a format, go back to main menu if hitting 0 
    """
    print("")    
    print("Arrival Airfield")
    print("")
    print("  \>")
    print("===\===")
    print("    \   ")
    print("________")
    print("")
    arr = input("Arrival Airfield - Enter ICAO code like (EIDW, EIWT, EICK): ")
    data.append(arr)
    registration()


def departure():
    """
    Logging Departure Airfield as part of Log a Flight journey
    Check if its a 4 letters format, go back to main menu if hitting ` 
    """
    print("")    
    print("Departure Airfield")
    print("")
    print(" ===/===")
    print("  </   ")
    print("________")
    print("")
    while True:
        dep = input("Departure Airfield - Enter ICAO code like (EIDW, EIWT, EICK): ")
        if dep == "`":
            print("")
            print("Logging process cancelled, back to main menu!\n")
            menu()
        if len(dep) != 4 or not dep.isalpha():
            print("")
            print("Departure A/P should be four letters Only!\n")
        else:
            data.append(dep.upper())
            arrival()
            break



menu()
"""
Main Menu
"""
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
        #option 4 - calculate time left in Engine
        engine_time_left()
        break
    elif option == 5:
        #option 5 - log a flight
        departure()
        break
    else:
        print("")
        print("Invalid option.")
    print()
    menu()
    option = int(input("Entert your option: "))


print("Thanks for using this program!")

