# Homework 1
# Nick Johnson
# npj190000
# CS 4395.001

# necessary imports for this assignment
import pathlib
import pickle
import sys
import re


class Person:  # Person class
    def __init__(self, last, first, mi, id, phone):  # init method
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    def display(self):  # display method
        print('\nEmployee id: ' + self.id)
        print("\t""\t" + self.first + " " + self.mi + " " + self.last)
        print("\t""\t" + self.phone)


def process_lines(person_list):  # process_lines function
    persons = {}  # initializing persons dict
    for line in person_list:  # iterate through each line of the list of people that you take in
        line = line.split(',')  # split each line on comma to get fields as text variables
        line[0] = line[0].capitalize()  # force first letter in last name to be uppercase
        line[1] = line[1].capitalize()  # force first letter in first name to be uppercase
        line[2] = line[2].upper()  # force middle initial to be uppercase
        if line[2] == '':  # if middle initial field is empty,
            line[2] = 'X'  # fill it in with 'X'
        id_match = re.search("^[a-zA-Z]{2}[0-9]{4}$", line[3])  # checking to see if ID is in proper regex form
        if not id_match:  # if ID is invalid, keep prompting user to enter a correctly formatted ID until
            # they do
            print("ID invalid: " + line[3])
            print("ID is two letters followed by 4 digits")
            while True:
                try:
                    possibly_fixed_id = input("Please enter a valid id: ")
                except ValueError:
                    print("ValueError")
                if not re.search("^[a-zA-Z]{2}[0-9]{4}$", possibly_fixed_id):
                    print("ID invalid: " + possibly_fixed_id)
                    print("ID is two letters followed by 4 digits")
                    continue
                else:
                    line[3] = possibly_fixed_id  # assign ID field to the correctly fixed ID inputted by the user
                    break
        phone_match = re.search("^[0-9]{3}-[0-9]{3}-[0-9]{4}$", line[4])  # checking to see if phone is in proper regex
        if not phone_match:  # if phone is invalid, keep prompting user to enter correctly formatted phone until
            # they do
            print("Phone " + line[4] + " is invalid")
            print("Enter phone number in form 123-456-7890")
            while True:
                try:
                    possibly_fixed_phone = input("Enter phone number: ")
                except ValueError:
                    print("ValueError")
                if not re.search("^[0-9]{3}-[0-9]{3}-[0-9]{4}$", possibly_fixed_phone):
                    print("Phone " + possibly_fixed_phone + " is invalid")
                    print("Enter phone number in form 123-456-7890")
                    continue
                else:
                    line[4] = possibly_fixed_phone  # assign phone field to correctly fixed phone inputted by the user
                    break
        line = Person(line[0], line[1], line[2], line[3], line[4])  # create a person object for each line
        persons[line.id] = line  # create new entry in persons dict where id is the key and Person object is the value

    return persons  # return the dict


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter a filename as a system arg')
        quit()

    rel_path = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(rel_path), 'r') as f:
        text_in = f.read().splitlines()

    employees = process_lines(text_in[1:])  # ignore heading line

    # pickle the employees
    pickle.dump(employees, open('employees.pickle', 'wb'))

    # read the pickle back in
    employees_in = pickle.load(open('employees.pickle', 'rb'))

    # output employees
    print('\n\nEmployee list:')

    for emp_id in employees_in.keys():
        employees_in[emp_id].display()
