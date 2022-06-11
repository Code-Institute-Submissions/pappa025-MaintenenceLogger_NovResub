# Maintenance Logger

### Milestone Project 3 - Python

My third Milestone Project is a simple Flight Logger program for a Flight Club. Despite its mandatory to log your flights on paper, many  pilots and clubs have their record in electronic form. With this handy little program you can log your flight to a linked Google Sheet which can be accessable for other Club Members to track the engine time left in the Aircraft and have a backup of your records as well.


## UX

When you start the program below the Welcome text appears the Menu. Here we can choose of the following options:

Information of navigation - few words about the keys needed to run the program

Check last Engine Maintenance - fetching data from Google Sheets about last service time

Check the coming Engine Maintenance - next service of the engine

Log a Flight - step by step guide to log your recent flight and save it to Google Sheets

Exit option

## Features

The following is a summary of the features already in place and those that could perhaps be implemented in the future.

### Existing Features

# Information and Service Time checks

Simple features with data obtained from Google Sheets after information provided we can choose another option in the Menu.

If we start the Log a Flight Jorney we are prompted to input the details of our most recent flight

# Deaprting Airport: 

Asked the 4 letters ICAO code of Depoarture Airport, program checking if we key in 4 characters. Answer is saved as all capital letters to Google Sheets. If we press ` anytime at different stages of Logging we will be back to Main Menu without saving the flight.

# Arrival Airport: 

Asked again the 4 letter ICAO code and save the details similarly as previous section.

# Registration: 

User prompted to key in the last 3 letters of Aircraft Registration. EI (as civil registration in Ireland) is prepopulated. Program checks if 3 letters were keyed in.

# Number of Takeoffs and Landings: 

This is the same number (in most cases), so we are just asked once to key in a number. Program checking if the entry is a whole number.

# Flight-time: 

Prompted to log your flight-time in hours (like 1.3, 0.5 etc..)

# Saving to Sheet phase: 

Out of logged hours program calculates a theoretical flight cost based on an hourly rate of €160 and save the imputted datas to Google Sheets.

### Features to Implement

Theoretically endless the improvement possibilities: if needed we can calculate time left in engine (hours left to next service), can make more detailed sheet with type of hour we flew (IFR or VFR) or we can add pilot function time as well (Solo, Dual etc). The code presented can be easily expanded for future needs.

## Testing

Page has been tested with pep8online checker and no errors were found.

Also long hours were spent to find bugs and experiment with different solutions for character checkings, logical orders of processes resulting a faily steady software.

### Technologies Used

- [python]( https://www.python.org/)

## Deployment

Deployment and source control was entirely done via GitHub. The repository can be found here:

Repo: https://github.com/pappa025/MaintenenceLogger

Project has been deployed in Heroku:

Heroku: https://maintenancelog.herokuapp.com/



