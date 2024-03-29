student_list = []


def create_student():
    name = input("Please enter the new student's name: ")
    student_data = {
        'name': name,
        'marks': []
    }

    return student_data


def add_marks(student, mark):
    student['marks'].append(mark)


def calculate_average_mark(student):
    number = len(student['marks'])
    if number == 0:
        return 0

    total = sum(student['marks'])
    return total / number


s = create_student()
print(calculate_average_mark(s))
add_marks(s, 5)
print(calculate_average_mark(s))
add_marks(s, 10)
print(calculate_average_mark(s))

def print_student_details(student):
    print("{}, average mark: {}. ".format(student['name'],
                                          calculate_average_mark(student)))


def print_student_list(students):
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        print_student_details(student)
        print(calculate_average_mark(student))


def menu():
    selection = input("Enter 'p' to print the student list, "
                      "'s' to add a new student, "
                      "'a' to add a mark to a student, "
                      "or 'q' to quit. "
                      "Enter your selection: ")

    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input("Enter the student ID to add a mark to: "))
            student = student_list[student_id]
            new_mark = int(input("enter the new mark to be added: "))
            add_marks(student, new_mark)

        selection = input("Enter 'p' to print the student list, "
                          "'s' to add a new student, "
                          "'a' to add a mark to a student, "
                          "or 'q' to quit. "
                          "Enter your selection: ")


menu()
import random

def is_road_straight():
    # Simulate whether the road is straight or not
    return random.choice([True, False])

def is_building_in_corner():
    # Simulate whether there is a building in the corner or not
    return random.choice([True, False])

def walk():
    print("Walking...")

def check_google_maps():
    print("Removing phone from pocket and checking Google Maps...")

# Loop until a building is found in the corner
while not is_building_in_corner():
    # Check if the road is straight
    while is_road_straight():
        walk()
        

    # Once the road is not straight, check Google Maps
    check_google_maps()

# Building found in the corner
print("Found a building in the corner!")
