#Use datetime module to handle anything to do with date/time
import datetime
import json  # If we are doing file I/O
import sqlite3  # If we are doing database
from random import seed
from random import randint
#Note: I will refer to data storage as database for now, regardless if we are storing it in a file system
#Note2: Make sure you create new feature on a new branch instead of master
"""Global Function"""
# this function is to generate the request and user id's, it takes a letter as an argument - either "U" for user or "R" for request


def gen_rand_num(id_type):
    user_id = id_type.upper()
    seed(1)
    # generate some integers
    for _ in range(4):
        value = randint(0, 10)
        user_id += str(value)
    return user_id


"""Classes"""


class User:
    pass
    ### NOTE: Make everything case insensitive so convert all strings into upper-case?
    #Attributes:
            # 1. ID (alphanumerical - U0001)
        # 2. Name (str)
        # 3. Birthdate (int - ex. 05241990)
        # 4. Location (str)
        # 5. Contribution Points (int)
        # 6. List of submitted requests (list of objects)

    # Methods

    def __init__(self, name, birthdate, location):
        pass
      self._user_id = id_generator("U") # create a unique user ID
      self._name = name
      self._birthdate = birthdate
      self._location = location
      self._contribution_pt = 0         # user starts with 0 contribution_pt
      self._submitted_requests = []     # contains ALL of user's submitted requests, from all 3 statuses ("OPEN" / "CLAIMED" / "FINISHED")
      
    def get_ID(self):
        pass
      return self._user_id
      
    def get_name(self):
        pass
      return self._name
      
    def get_birthdate(self):
        pass
      return self._birthdate
      
    def get_contribution_pt(self):
        pass
      return self._contribution_pt
      
    def get_submitted_requests(self):
        pass
      return self._submitted_requests
      
    def update_name(self, new_name):
        pass
      # called by Community - update_info()
      self._name = new_name       # new_name (str)
      
    def update_birthdate(self, new_birthdate):
        pass
      # called by Community - update_info()
      self._name = new_birthdate   # new_birthdate (int)
      
    def update_location(self, new_location):
        pass
      # called by Community - update_info()
      self._update_location = new_location  # new_location (str)
      
    def add_submitted_request(self, request_id? or Request):
        pass
      # add to self._submitted_requests
      
    def del_submitted_request(self, request_id):
        pass
      # delete from self._submitted_requests
      
    def print_submitted_requests(self):
        pass
        # prints list of submitted request objects (oldest to newest?) with all of the attributes (might need _repr_?)
      
class Request:
    pass
    #Attributes:
        1. request_id (alphanumerical: R0001)
        2. subject (str)
        3. deadline (date/time)
        4. post_detail (str)
        5. post_date (date/time)
        6. completed_by (initialized to None but will be set to the contributor ID that completed the request)
        7. requested_by (initialized to the user_id of the requestor)
        8. status (str - "OPEN", "CLAIMED", or "FINISHED")
        
    # Methods
            def __init__(self, subject, deadline, post_detail):
                self._request_id = id_generator("R")  #calls the id_generator to generate the unique ID
            self._subject = subject
            self._deadline = deadline
            self._post_detail = post_detail
            self._post_date = #assign post date using date/time 
            self._completed_by = None
            self._requested_by = 
            self._status = "OPEN"
            
        # Getters
        get_request_id
        get_subject_id
        get_deadline
        get_post_detail
        get_post_date
        get_completed_by
        get_requested_by
        get_status
        
        # Setters
        set_deadline 
        set_post_detail
        set_completed_by
        set_status
        
            
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
    #Raise TypeError if user inputs invalid type for any attribute
        #Reprompt user to enter information again
      
    #Generate unique ID for the user --> gen_ran_num("U")
    #Instantiate new object and store the information --> User(name, birthdate, location)
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
        #Raise InvalidID error
            #Prompt user to either enter another ID or register
            # If user choooses to enter another ID --> login()
            # If user chooses to register --> register()
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
