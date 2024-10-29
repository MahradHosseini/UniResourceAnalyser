from Course import *
from LabCourse import *
from University import University
import sys

EXIT = 7 # The exit option in the menu

if __name__ == "__main__":

    # Checking argument's existence
    if len(sys.argv) < 3:
        print("Please provide two file names as arguments.")
        sys.exit(1)

    departmentsFile = sys.argv[1]
    coursesFile = sys.argv[2]

    # Loading the data to appropriate objects
    METU = University("METU", "NCC")
    METU.loadUniversity(departmentsFile, coursesFile)
    print("University successfully loaded.")

    # Initiating the Menu loop
    menu = 0
    while menu != EXIT:
        print("\n1. Print all the lab courses")
        print("2. Print department sizes")
        print("3. Print instructor courses")
        print("4. Print unpopulated courses")
        print("5. Print multi-section courses")
        print("6. Print top course(s)")
        print(f"{EXIT}. Exit")

        # Getting the input while checking for the Value Error (will raise if the input is not an integer)
        try:
            menu = int(input("Enter your choice: "))
        except ValueError:
            print("!!!! PLEASE ENTER A VALID NUMBER !!!!")
            continue

        # Implementing a switch-like behaviour for the menu
        if menu == 1:
            METU.printLabCourses()
        elif menu == 2:
            METU.printDepartmentSizes()
        elif menu == 3:
            METU.printInstructorCourses()
        elif menu == 4:
            METU.printUnpopulatedCourses()
        elif menu == 5:
            METU.printMultiSectionCourses()
        elif menu == 6:
            METU.printTopCourses()
        elif menu == EXIT:
            print("Goodbye!")
        else:
            print("!!!! PLEASE ENTER A VALID OPTION !!!!")

