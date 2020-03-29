import sqlite3
from Classes import User, Request
import data_handling as db

"""Other features"""
def account_management(user):
    while True:
        print("\nUser information")
        print("Name: {}".format(user._name))
        print("Date of Birth: {}".format(user._birthdate))
        print("Adress: {}\n".format(user._location))

        choice = int(input("Would you like to 1.Update your info 2.Check submitted request 3.Check claimed request 4.Quit: "))
        print("")

        if (choice == 1):
            change_info = int(input("Which information would you like to change? 1.Name 2.DOB 3.Adress 4.Quit: "))
            print("")

            if (change_info == 1):
                new_name = input("Enter a new name: ")
                user._name = new_name
                db.update_info(user, change_info, new_name)
            elif (change_info == 2):
                new_birthdate = input("Enter a new birthdate: ")
                user._birthdate = new_birthdate
                db.update_info(user, change_info, new_birthdate)
            elif (change_info == 3):
                new_location = input("Enter a new location: ")
                user._location = new_location
                db.update_info(user, change_info, new_location)
            else:
                return user
        elif (choice == 2):
            request_list = db.retrieve_submitted_request(user)
            if (len(request_list) > 0):
                for request_index in range(len(request_list)):
                    print("")
                    request = request_list[request_index]
                    print("{}. {}".format(request_index + 1, request._subject))
                    print("Request ID: {}".format("Completed" if request_list[request_index]._completed == "True" else "Incomplete"))
                    print("Status: {}".format(request._completed))
                    print(request._post_detail)

                    return
            else:
                print("It seems like you have not submitted any request yet! You can submit request through the request section.\n")
        elif (choice == 3):
            request_list = db.retrieve_claimed_request(user)
            if (len(request_list) > 0):
                for request_index in range(len(request_list)):
                    print("")
                    request = request_list[request_index]
                    print("{}. {}".format(request_index + 1, request._subject))
                    print("Request ID: {}".format("Completed" if request_list[request_index]._completed == "True" else "Incomplete"))
                    print("Status: {}".format(request._completed))
                    print(request._post_detail)

                    return
            else:
                print("It seems like you have not claimed any request yet! You can claim request through the contribute section.\n")
        elif (choice == 4):
            return
        else:
            print("Invalid Input.\n")

#Parameter: User() object
def check_leaderboard(user):
    #Retrieve users, sorted by contribution points
    user_list = db.retrieve_users_by_points()

    #Print out top 10 users
    for i in range(len(user_list)):
        print("{}. {} with {} points".format(i + 1, user_list[i]._name, user_list[i]._contribution_pt))

    print("")
""""""



"""Request and Contribute"""
#Description: Let the user post a request
#Parameter: User object
def request_board(user):
    print("Welcome to the request board! Enter the following information and your request will be posted.")
    
    subject = input("Request subject: ")
    detail = input("Detail: ")
    
    request = Request(subject, detail, user)
    db.store_request(request)

def print_request(request_list):
    for request_index in range(len(request_list)):
        print("")
        request = request_list[request_index]
        print("{}. {}".format(request_index + 1, request._subject))
        print("Request ID: {}".format(request._request_id))
        print(request._post_detail)
    print("")


#Description: Let the user claim a request or check of a request
#Parameter: User object
#Return type: Void
def contribute_board(user):
    option = int(input("Would you like to 1.Claim an open request 2.Checkoff completed request: "))
    if (option == 1):
        while True:
            method = int(input("How would you like to search for result? 1.See top 10 result 2.Search for keyword 3.Quit: "))

            if (method == 1):
               request_list = db.retrieve_available_requests()
            elif (method == 2):
               keyword = input("\nEnter your keyword: ")
               request_list = db.search_for_keyword(keyword)
            elif (method == 3):
                return
            else:
               print("Invalid input.")
               continue
              
            if (len(request_list) > 0):
                print_request(request_list)
            else:
                print("Seems like there is no request right now. Feel free to come back later!\n")
                return
                
            request_id = input("Enter request ID to pick up task or '0' to quit: ")
            request_id = request_id.upper()
            
            if (request_id == "0"):
              break
            elif (request_id[0] == "R"):
              for request_index in range(len(request_list)):
                request = request_list[request_index]
                if (request._request_id == request_id):
                  request._claimed_by = user._user_id
                  db.claim_request(request) #Update database
                  print("\nThank you for making this community a better place. We appreciate it!")
                  return
              print("Request not found.")
            else:
              print("Invalid input.")
    elif (option == 2):
        request_list = db.retrieve_claimed_request(user)

        if(len(request_list) > 0):
            print_request(request_list)
        else:
            print("Seems like you haven't picked up any request yet. Feel free to help someone out!")
            return

        claimed_id = input("Enter request ID to check off task or '0' to quit: ")
        claimed_id = claimed_id.upper()

        if (claimed_id == "0"):
            return
        elif (claimed_id[0] == "R"):
            for request_index in range(len(request_list)):
              request = request_list[request_index]
              if (request._request_id == claimed_id):
                request._status = "True"
                user._contribution_pt += 100
                db.check_off_request(request, user) #Update database
                print("\nWell Done! You earned 100 points!")
                return
            print("Request not found.")
        else:
            print("Invalid input.")
    else:
        print("Invalid input.")
        contribute_board(user)
""""""



"""Register and Login"""
#Description: Let the user register, store info in database
#Return type: User() object
def register():
    print("Thank you for registering! Please enter the following information:")
    
    #Ask user for name, birthdate, and location
    name = input("Name: ")
    birthdate = input("Birthdate: ")
    location = input("Address: ")
      
    #Instantiate new object and store the information --> User(name, birthdate, location)
    current_user = User(name, birthdate, location)
    #Store user information in json/database --> store_data(user)
    db.store_user(current_user)

    return current_user

#Description: Prompt user for login ID, return all the user information
#Return type: User() object or None   
def login():
    userID = input("Please enter your UserID: ")
    userID = userID.upper()
    
    #Find user in database with the given ID
    user = db.retrieve_user_from_id(userID)
    
    if user != None:
    	return user
    else:
    	print("User not found. Did you type in the right ID?")
    	return None
    
""""""



"""Main and Exit Program"""
def exit_program():
    print("Thank you for using Community Request Board. We hope to see you again!")
    exit()
    
def main():
    pass
    # Print welcome message
    print("Welcome to Community Request Board!\n")
    
    while True:
      signin_option = int(input("Please enter 1 to Login and 2 to Register: "))

      if (signin_option == 1):
        current_user = login()
        if(current_user == None):
        	continue
        else:
        	print("\nLogin Successful. Welcome {}!\n".format(current_user._name))
        	break
      elif (signin_option == 2):
        current_user = register()
        print("\nRegistration Successful. Welcome {}!\n".format(current_user._name))
        print("Your userID is {}. Please remember that to login.\n".format(current_user._user_id))
        break
      else:
        print("Invalid input.")
    
    while True:
      menu_option = int(input("Please choose if you would like to 1.Request 2.Contribute 3.Others 4.Exit: "))
      print("")
      
      if (menu_option == 1):
        request_board(current_user)
        print("\nThank you for posting your request. Someone will pick it up soon!\n")
      elif (menu_option == 2):
        contribute_board(current_user)
      elif (menu_option == 3):
        other_option = int(input("Please choose if you would like to 1.Manage your account 2.Check the leaderboard 3.Go back: "))
        
        if (other_option == 1):
          current_user = account_management(current_user)
        elif (other_option == 2):
          check_leaderboard(current_user)
        elif (other_option == 3):
          continue
        else:
          print("\nInvalid input.\n")
      elif (menu_option == 4):
        exit_program()
      else:
        print("\nInvalid input.\n")
            
if __name__ == '__main__':
    #db.create_table()
    main()
    db.conn.commit()
    db.conn.close()  
""""""