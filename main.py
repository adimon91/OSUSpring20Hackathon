import sqlite3
from user_and_request import User, Request

conn = sqlite3.connect("database.db")
c = conn.cursor()



"""Data Handling"""
#Description: Create database table
def create_table():
    c.execute("""CREATE TABLE user_table (
             userid text PRIMARY KEY,
             name text,
             birthdate text,
             location text,
             contribution_pt integer
             )""")

    c.execute("""CREATE TABLE request_table (
             request_id text,
             subject text,
             post_detail text,
             claimed_by text,
             requested_by text,
             completed text
             )""")

    conn.commit()

"""User table"""
#Description: Store user into a table
#Parameter: User object
def store_user(user):
  c.execute("INSERT INTO user_table VALUES (:user_id, :name, :birthdate, :location, :contribution_pt)", {
            'user_id': user._user_id,
            'name': user._name,
            'birthdate': user._birthdate,
            'location': user._location,
            'contribution_pt': user._contribution_pt})
    
  conn.commit()
    
#Description: Get top 10 users in the order of contribution_point
#Return type: list of User object
def retrieve_users_by_points():
    c.execute("SELECT * FROM user_table ORDER BY contribution_pt DESC")
    user_list = []
    users = c.fetchmany(10)

    for i in range(len(users)):
        user_list.append(User(users[i][1], users[i][2], users[i][3], users[i][4], users[i][0]))

    return user_list

#Description: Get the user object based given their userID
#Parameter: string
#Return type: User object
def retrieve_user_from_id(ID):
  if(ID[0] == 'U'):
    c.execute("SELECT * FROM user_table WHERE userid = ?", (str(ID),))
    user = c.fetchone()
  else:
    return None

  if user != None:
    return User(user[1], user[2], user[3], user[4], user[0])
  else:
    return None

#Description: Update user info in the database
def update_info(user, option, new_info):
    if (option == 1):
        c.execute("""UPDATE user_table
                    SET name = ?
                    WHERE userid = ?""", (new_info, user._user_id))
    elif (option == 2):
        c.execute("""UPDATE user_table
                    SET birthdate = ?
                    WHERE userid = ?""", (new_info, user._user_id))
    elif (option == 3):
        c.execute("""UPDATE user_table
                    SET location = ?
                    WHERE userid = ?""", (new_info, user._user_id))
    conn.commit()  
""""""

"""Request table"""
#Description: Store request in database
#Parameter: Request object
def store_request(request):
    c.execute("INSERT INTO request_table VALUES (:request_id, :subject, :post_detail, :claimed_by, :requested_by, :completed)",
    {'request_id': request._request_id, 
     'subject': request._subject,
     'post_detail': request._post_detail,
     'claimed_by': "False",
     'requested_by': request._requested_by._user_id,
     'completed': "False"})
    
    conn.commit()

#Description: Set the user who claimed the request
#Parameter: Request object
def claim_request(request):
    c.execute("""UPDATE request_table
                SET claimed_by = ?
                WHERE request_id = ?""", (request._claimed_by, request._request_id))
    conn.commit()  
    
#Description: Set request as completed, add points to user
#Parameter: Request object, User object
def check_off_request(request, user):
    c.execute("""UPDATE request_table
                SET completed = ?
                WHERE request_id = ?""", ("True", request._request_id))
    c.execute("""UPDATE user_table
                SET contribution_pt = ?
                WHERE userid = ?""", (user._contribution_pt, user._user_id))
    conn.commit()  

#Description: Take a list of tuple and convert it to a list of Request object
#Parameter: A list of tuple
#Return type: A list of Request object
def convert_to_list_of_object(request_list):
    list_of_object = []
    for i in range(len(request_list)):
        request_by = retrieve_user_from_id(request_list[i][2])
        if (request_list[i][3] != None):
            claimed_user = retrieve_user_from_id(request_list[i][3])
        else:
            claimed_user = None
        list_of_object.append(Request(request_list[i][1], request_list[i][2], request_by, request_list[i][0], claimed_user, request_list[i][5]))

    return list_of_object

#Description: Retrieve requests that have not been claimed yet
#Return type: A list of Request object
def retrieve_available_requests():
    c.execute("SELECT * FROM request_table WHERE claimed_by = ?", ("False",))
    request_list = c.fetchmany(10)
    list_of_object = convert_to_list_of_object(request_list)

    return list_of_object

#Description: Retrieve requests that is claimed by the user but is not yet completed
#Parameter: User object
#Return type: A list of Request object
def retrieve_claimed_request(user):
    c.execute("SELECT * FROM request_table WHERE claimed_by = ? AND completed = ?", (user._user_id, "False"))
    request_list = c.fetchall()
    list_of_object = convert_to_list_of_object(request_list)

    return list_of_object

#Description: Retrieve requests that is claimed by the user
#Parameter: User object
#Return type: A list of Request object
def retrieve_claimed_request(user):
    c.execute("SELECT * FROM request_table WHERE claimed_by = ?", (user._user_id, ))
    request_list = c.fetchall()
    list_of_object = convert_to_list_of_object(request_list)

    return list_of_object

#Description: Retrieve requests that is posted by the user
#Parameter: User object
#Return type: A list of Request object
def retrieve_submitted_request(user):
    c.execute("SELECT * FROM request_table WHERE requested_by = ?", (user._user_id,))
    request_list = c.fetchall()
    list_of_object = convert_to_list_of_object(request_list)

    return list_of_object

#Description: Retrieve requests that matches the keyword
#Parameter: string
#Return type: A list of Request object
def search_for_keyword(keyword):
    c.execute("SELECT * FROM request_table WHERE claimed_by = ? AND (post_detail LIKE ? OR subject LIKE ?)", ("False", '%{}%'.format(keyword), '%{}%'.format(keyword)))
    request_list = c.fetchall()
    list_of_object = convert_to_list_of_object(request_list)

    return list_of_object
""""""
"""End of data handling"""



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
                update_info(user, change_info, new_name)
            elif (change_info == 2):
                new_birthdate = input("Enter a new birthdate: ")
                user._birthdate = new_birthdate
                update_info(user, change_info, new_birthdate)
            elif (change_info == 3):
                new_location = input("Enter a new location: ")
                user._location = new_location
                update_info(user, change_info, new_location)
            else:
                return user
        elif (choice == 2):
            request_list = retrieve_submitted_request(user)
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
            request_list = retrieve_claimed_request(user)
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
    user_list = retrieve_users_by_points()

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
    store_request(request)

#Description: Let the user claim a request or check of a request
#Parameter: User object
#Return type: Void
def contribute_board(user):
    option = int(input("Would you like to 1.Claim an open request 2.Checkoff completed request: "))
    if (option == 1):
        while True:
            method = int(input("How would you like to search for result? 1.See top 10 result 2.Search for keyword 3.Quit: "))

            if (method == 1):
               request_list = retrieve_available_requests()
            elif (method == 2):
               keyword = input("\nEnter your keyword: ")
               request_list = search_for_keyword(keyword)
            elif (method == 3):
                return
            else:
               print("Invalid input.")
               continue
              
            if (len(request_list) > 0):
                for request_index in range(len(request_list)):
                    print("")
                    request = request_list[request_index]
                    print("{}. {}".format(request_index + 1, request._subject))
                    print("Request ID: {}".format(request._request_id))
                    print(request._post_detail)
            else:
                print("Seems like there is no request right now. Feel free to come back later!\n")
                return
                
            request_id = input("Enter request ID to pick up task or '0' to quit: ")
            
            if (request_id == "0"):
              break
            elif (request_id[0] == "R"):
              for request_index in range(len(request_list)):
                request = request_list[request_index]
                if (request._request_id == request_id):
                  request._claimed_by = user._user_id
                  claim_request(request) #Update database
                  print("\nThank you for making this community a better place. We appreciate it!")
                  return
              print("Request not found.")
            else:
              print("Invalid input.")
    elif (option == 2):
        request_list = retrieve_claimed_request(user)

        if(len(request_list) > 0):
            for request_index in range(len(request_list)):
                print("")
                request = request_list[request_index]
                print("{}. {}".format(request_index + 1, request._subject))
                print("Request ID: {}".format(request._request_id))
                print(request._post_detail)
            print("")
        else:
            print("Seems like you haven't picked up any request yet. Feel free to help someone out!")
            return

        claimed_id = input("Enter request ID to check off task or '0' to quit: ")

        if (claimed_id == "0"):
            return
        elif (claimed_id[0] == "R"):
            for request_index in range(len(request_list)):
              request = request_list[request_index]
              if (request._request_id == claimed_id):
                request._status = "True"
                user._contribution_pt += 100
                check_off_request(request, user) #Update database
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
    store_user(current_user)

    return current_user

#Description: Prompt user for login ID, return all the user information
#Return type: User() object or None   
def login():
    userID = input("Please enter your UserID: ")
    userID = userID.upper()
    
    #Find user in database with the given ID
    user = retrieve_user_from_id(userID)
    
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
    #create_table()
    main()
    conn.commit()
    conn.close()  
""""""