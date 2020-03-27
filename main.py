#Use datetime module to handle anything to do with date/time
import datetime

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
#Parameter: string, string
#Return type: *Depends on storing method
def retrieve_data(table_name, column = '*'):
    pass
    #1. Retrieve a list of data from the specified table name and column
    #2. Return the list of retrieved data

#Parameter: Request() object
def print_request(request):
    pass
    #Print out requests in following format
        #1. ID
        #2. subject
        #3. deadline
        #4. post detail
""""""


"""Search/Sort Algorithm"""
#Note: The algorithm does not have to be fast

#Parameter: list
#Return type: list
def search_for_location(request_list):
    pass

#Parameter: list
#Return type: list
def sort_by_dealine(request_list):
    pass

#Parameter: list
#Return type: list
def search_for_keyword(request_list):
    pass

#Parameter: list
#Return type: list
def sort_by_points(user_list):
    pass
""""""


"""Other features"""
def update_info():
    pass
    #Ask user which info they like to change
        #1. Name
        #2. birthdate
        #3. location

    #Update the information in the database

def check_current_request():
    pass
    #Get a list of request that the user has picked

    #Loop:
        #Print out all the request --> print_request(request_object)

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
    #Get data from database --> retrieve_data(table_name, column)

    #Let user choose how they want to look for request
        #1. Same location --> search_for_location()
        #2. How close the deadline is --> sort_by_dealine()
        #3. Look for keyword --> search_for_keyword()

    #Print lists of tasks --> print_request(request_object)

    #Let user choose a task by inputing ID or use another search method
""""""


"""Register and Login"""
def register():
    pass
    #Ask user for name, birthdate(cause why not), location
    #Do error handling, if input is valid then proceed

    #Store user information in json/database
    #Generates unique ID for the user

def login():
    pass
    #Ask user for their ID

    #Get data from database --> retrieve_data(table_name, column)
    #Compare user input to all the retrieved ID

    #If matched: break and return a user object with all the detailed filled in
    #Else: invalid id, reprompt user to enter another ID or register
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
    #if register --> register()
    #else --> login()

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
