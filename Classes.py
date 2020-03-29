from random import randint

def gen_rand_num(id_type):
    user_id = id_type.upper()
    # generate some integers
    for _ in range(6):
        value = randint(0, 10)
        user_id += str(value)
    return user_id

class User:
    def __init__(self, name, birthdate, location, contribution_pt=0, user_id=gen_rand_num("U")):
        self._user_id = user_id  # create a unique user ID
        self._name = name
        self._birthdate = birthdate
        self._location = location
        self._contribution_pt = contribution_pt


class Request:
    def __init__(self, subject, post_detail, requested_by, request_id=gen_rand_num("R"), claimed_by= "False", completed = "False"):
        self._request_id = request_id  # calls the id_generator to generate the unique ID
        self._subject = subject
        self._post_detail = post_detail
        self._claimed_by = claimed_by
        self._requested_by = requested_by
        self._completed = completed



