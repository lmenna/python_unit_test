# application_code.py
#
# unittest example.  Define a person class that will be used to show
# how to run unit tests using Python's built in unittest.
#
# To run the application use the command,
#
# > python person.py
#
# To run the unit tests use the command,
#
# > python -m unittest test_person

class Person:
    name = []

    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1

    def get_name(self, user_id):
        if user_id >= len(self.name):
            return 'There is no such user'
        else:
            return self.name[user_id]


if __name__ == '__main__':
    person = Person()
    print('User Luigi has been added with id ', person.set_name('Luigi'))
    print('User associated with id 0 is ', person.get_name(0))
    
