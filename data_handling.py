import sqlite3
from Classes import User, Request

conn = sqlite3.connect("sqlite.db")
c = conn.cursor()

"""Data Handling"""
#Description: Create database table
def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS user_table (
             userid text PRIMARY KEY,
             name text,
             birthdate text,
             location text,
             contribution_pt integer
             )""")

    c.execute("""CREATE TABLE IF NOT EXISTS request_table (
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
    users = c.fetchall()

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