from Course import *
from LabCourse import *
from University import University
import sys

EXIT = 7

def LoadCourses():
    courses = {}

    with open("courses.txt", "r") as file:
        lines = file.readlines()

        for line in lines[1:]:
            parts = line.split(",")

            departmentCode = parts[0]
            courseCode = parts[1]
            courseName = parts[2]
            instructor = parts[3]
            section = parts[4]
            capacity = int(parts[5])
            registeredStudents = int(parts[6])

            # Determine if the section is a lab
            is_lab = "Lab" in section

            # Check if the course already exists in the dictionary
            if courseCode in courses:
                course = courses[courseCode]
                # If the course is a regular Course but we encounter a lab, upgrade to LabCourse
                if is_lab and not isinstance(course, LabCourse):
                    # Upgrade to LabCourse, preserving existing sections
                    new_course = LabCourse(course.ccode, course.cname)
                    new_course.sections = course.sections  # Copy existing sections
                    courses[courseCode] = new_course
                    course = new_course
            else:
                # Create a new LabCourse if it's a lab, otherwise create a regular Course
                if is_lab:
                    course = LabCourse(courseCode, courseName)
                else:
                    course = Course(courseCode, courseName)
                courses[courseCode] = course

            # Add the section to the course
            if is_lab:
                course.addLabSection(section, capacity, registeredStudents, instructor)
            else:
                course.addSection(section, capacity, registeredStudents, instructor)
    return courses


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

    menu = 0
    while menu != EXIT:
        print("\n1. Print all the lab courses")
        print("2. Print department sizes")
        print("3. Print instructor courses")
        print("4. Print unpopulated courses")
        print("5. Print multi-section courses")
        print("6. Print top course(s)")
        print(f"{EXIT}. Exit")

        try:
            menu = int(input("Enter your choice: "))
        except ValueError:
            print("!!!! PLEASE ENTER A VALID NUMBER !!!!")
            continue

        if menu == 1:
            METU.PrintLabCourses()
        elif menu == 2:
            METU.PrintDepartmentSizes()
        elif menu == 3:
            METU.PrintInstructorCourses()
        elif menu == 4:
            METU.PrintUnpopulatedCourses()
        elif menu == 5:
            METU.PrintMultiSectionCourses()
        elif menu == 6:
            METU.PrintTopCourses()
        elif menu == EXIT:
            print("Goodbye!")

        else:
            print("!!!! PLEASE ENTER A VALID OPTION !!!!")