#Use datetime module to handle anything to do with date/time
import datetime
import json #If we are doing file I/O
import sqlite3 #If we are doing database

#Note: I will refer to data storage as database for now, regardless if we are storing it in a file system
#Note2: Make sure you create new feature on a new branch instead of master

"""Classes"""
class User():
    pass
    #Attributes:
        #Name, birthdate, location
        #Contribution points
        #A list of IDs of selected request 

class Request():
    pass
    #Attributes:
        #1. ID
        #2. subject
        #3. deadline
        #4. post detail
""""""


"""Data Handling"""
#Parameter: string, User() or Request() object
def store_data(table_name, object):
    pass
    #Store the information in JSON file or database

#Parameter: string, string
#Return type: a list of object
def retrieve_data(table_name, column = '*'):
    pass
    #1. Retrieve a list of data from the specified table name and column
    #2. Return the list of object

def update_info():
    pass
    #Ask user which info they like to change
        #1. Name
        #2. birthdate
        #3. location

    #Update the information in the database

#Parameter: list of Request() object
def print_request(request):
    pass
    #Use a for loop:
        #Print out each request in the following format
            #1. ID
            #2. subject
            #3. deadline
            #4. post detail
""""""


"""Search/Sort Algorithm"""
#Note: The algorithm does not have to be fast

#Parameter: list of objects
#Return type: list of objects
def search_for_location(request_list):
    pass

#Parameter: list of objects
#Return type: list of objects
def sort_by_dealine(request_list):
    pass

#Parameter: list of objects
#Return type: list of objects
def search_for_keyword(request_list):
    pass

#Parameter: list of objects
#Return type: list of objects
def sort_by_points(user_list):
    pass
""""""


"""Other features"""
def check_current_request():
    pass
    #Get a list of request that the user has picked --> Retrieve data()
    #Print out all the request --> print_request(request_list)

#Parameter: User() object
def account_management(user):
    pass
    #Print user information:
        #Name, birthdate, location
        #Contribution point

    #Ask if they want to:
        #1. Edit info --> update_info
        #2. Check current requests --> check_request()
        #3. Go back to homepage

#Parameter: User() object
def check_leaderboard(user):
    pass
    #Retrieve all of users' name and their points --> retrieve_data(user_table, 'name, points')
    #Reorder the list by the points --> sort_by_points()
    #Print out top 10 users in the leaderboard and the placement of the current user 
""""""


"""Request and Contribute"""
def request_board():
    pass
    #Ask user for:
        #1. subject line 
        #2. request post(ideally no more than 45 words?)
        #3. deadline

    #If user input is valid
        #Generate unique request ID
        #Store request info in database, as well as, location and posted date

def contribute_board():
    pass
    #Get data from database --> request_list = retrieve_data(table_name, column)

    #Let user choose how they want to look for request
        #1. Same location to where they live --> search_for_location(request_list)
        #2. How close the deadline is --> sort_by_dealine(request_list)
        #3. Look for keyword --> search_for_keyword(request_list)

    #Print lists of tasks --> print_request(request_list)

    #Let user choose a task by inputing ID or use another search method
""""""


"""Register and Login"""
#Return type: User() object
def register():
    pass
    #Ask user for name, birthdate, and location
    #Do error handling, if input is valid then proceed
    #Generates unique ID for the user
    
    #Instantiate new object and store the information

    #Store user information in json/database --> store_data(user)
    #Return user

#Return type: User() object
def login():
    pass
    #Ask user for their ID

    #Get data from database --> retrieve_data(table_name, column)
    #Compare user input to all the retrieved ID

    #If matched: 
        #Instantiate user object
        #Fill in the information into user
        #Return user
    #Else: 
        #Invalid id, reprompt user to enter another ID or register
""""""


"""Main and Exit Program"""
def exit_program():
    pass
    #Print thank you message
    #exit()

def main():
    #Tip: use "ctrl + /" to comment/uncomment a line
    pass

    # Print welcome message

    #Let user choose to login or register
        #if register --> user = register()
        #else --> user = login()

    #While True:
        #Let user choose from the following
            #1. Request --> request_board()
            #2. Contribute --> contribute_board()
            #3. Others
            #4. Exit program --> exit_program()

        #If others, let user choose from the following
            #1. Account management --> account_management()
            #2. Check leaderboard --> check_leaderboard()

if __name__ == '__main__':
    main()
""""""
