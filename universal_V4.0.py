
import subprocess as sp

from student_app import StudentApp

def menu():
    """Displays a set of menu options for the user to select from
    """
    sp.call('clear', shell=True)
    print('-----'*6)
    print(' UL GRANT APPLICATION SYSTEM')
    print('-----'*6)
    print("\nA. Input Application Details for a Student. \
            \nB. Display Summary of Applications. \
            \nC. Display Grant Awardees. \
            \nX. Exit")

    while True:
        option = input().lower()

        # Validates menu options by checking if
        # the option input matches a list of stored options
        while option not in ['a', 'b', 'c', 'x']:
            print("Error!! Only option A, B, C & X are valid. Please try again:")
            break
        else:
            break

    if option == 'a':
        get_student_details()


def get_student_details():
    """Lets the user enter a set amount of student applications.
    """
    
    sp.call('clear', shell=True)
    print('\n')
    print('------'*5)
    print(" Student Application Details")
    print('------'*5)
    appMax = 0
    appMax += 1

    while appMax <= 25:
        stuName = input("Enter students full name: ")
        stuGPA = float(input("Enter Student GPA: "))
        tuition = float(input("Enter tuition: "))

        make_instance(stuName, stuGPA, tuition)

        display_student_details()
        select_menu_opt()


def make_instance(name, gpa, shortfall):
    """Takes in Student data and builds student application insances 

    Arguments:
        name {string} -- The name of a single student 
        gpa {float} -- Students GPA
        shortfall {float} -- The shortfall for one student 
    """

    studentInstance = StudentApp(name, gpa, shortfall)

    return studentInstance


def display_student_details():
    pass
    # view = StudentApp(stuname, stuGPA, tuition)
    # view.display()

    # return view


def select_menu_opt():
    """Lets the usere select weather to process another application,
       go back to the main menu or exit the program.
    """

    print("Do you wish to enter another application? [y/n]: ")
    opt = input()
    if opt == 'n':
        print('Return to the main menu? [y/n]')
        menuOpt = input()
        if menuOpt == 'n':
            exit()
        else:
            menu()
    else:
        get_student_details()


if __name__ == "__main__":
    menu()
