from Department import Department
from LabCourse import LabCourse
import re
import matplotlib.pyplot as plt


class University:
    def __init__(self, uname, ubranch):
        self.uname = uname
        self.ubranch = ubranch
        self.departments = []

    def loadUniversity(self, departmentsFilename, coursesFilename):
        try:
            file = open(departmentsFilename, "r")
        except IOError:
            print("File could not be opened")
            exit(1)
        file_departments = file.readlines()[1:]  # Skip the first line
        for i in range(len(file_departments)):
            # separating department name,shortname and code
            splited_departments = re.split(",", file_departments[i].strip())
            self.addDepartment(splited_departments[2], splited_departments[1], splited_departments[0])

        try:
            file = open(coursesFilename, "r")
        except IOError:
            print("File could not be opened")
            exit(1)
        file_courses = file.readlines()[1:]  # Skip the first line
        for i in range(len(file_courses)):
            # separating courses name,code, etc.
            splited_courses = re.split(",", file_courses[i].strip())
            # checking if the course code is in the following form CNG 445
            if re.match(r"^\w{3,4}\s\d{3,4}$", splited_courses[1]):
                # creating a new course object
                self.addCourseToDepartment(splited_courses)

    def addDepartment(self, dname, dshortname, dcode):
        # creating a new department object
        new_department = Department(dname, dshortname, dcode)
        # adding the new object to the departments list
        self.departments.append(new_department)

    def addCourseToDepartment(self, courseArray):
        # Extract relevant course information
        dcode, ccode, cname, instructor, section, capacity, registered = courseArray
        capacity, registered = int(capacity), int(registered)
        for department in self.departments:
            isLabCourse = 1
            # finding the right department to add the course through the department code
            if department.dcode == dcode:
                # checking if the course already exist in the courses and retrieving it
                existing_course = next((course for course in department.courses if course.ccode == ccode), None)
                # if course doesn't exist add new course
                if not existing_course:
                    # add section course
                    if re.match(r"S\d+", section):
                        isLabCourse = 0
                    department.addCourse(ccode, cname, isLabCourse)
                    existing_course = department.courses[-1]

                # adding section or lab section
                if re.match(r"S\d+", section):  # If section starts with "S", it's a regular section
                    existing_course.addSection(section, capacity, registered, instructor)
                else:
                    existing_course.addLabSection(section, capacity, registered, instructor)

    def printLabCourses(self):
        for department in self.departments:
            print(f"Department {department.dname}, Total Lab Capacity: {department.getTotalLabCapacity()}")
            for course in department.getLabCourses():
                print(course)

    def printDepartmentSizes(self):
        totalCapacityList = []
        depShortNameList = []
        for department in self.departments:
            totalCapacity = 0
            for course in department.courses:
                totalCapacity += course.getTotalCapacity()
            totalCapacityList.append(totalCapacity)
            depShortNameList.append(department.dshortname)
        plt.pie(totalCapacityList, labels=depShortNameList)
        plt.title('Department Sizes')
        plt.show()

    def printInstructorCourses(self):
        instructor_name = input("Please enter the instructors name: ")
        foundCourses = []
        # finding the course
        for department in self.departments:
            for course in department.courses:
                if any(instructor.lower() == instructor_name.lower() for instructor, _, _ in course.sections.values()):
                    foundCourses.append(course)
        # checking the number of courses the teachers teach
        if len(foundCourses) == 0:
            print("Given instructors name doesn't exist in the system")
            return
        if len(foundCourses) == 1:
            print(foundCourses[0])
        else:
            print("This instructor teaches more than 1 course,"
                  " please choose the course number you want from the following list: ")
            counter = 1
            # displaying the courses the teachers teach
            for course in foundCourses:
                print("(" + str(counter) + ") " + course.ccode + " - " + course.cname)
                counter += 1
            courseNumber = int(input("Choice: "))
            if 0 < courseNumber < counter:
                print(foundCourses[courseNumber - 1])
                return
            print("Invalid input")

    def printUnpopulatedCourses(self):
        for department in self.departments:
            print("\nDepartment: " + department.dname)
            unpopulatedCourses = department.getUnpopulatedCourses()
            for course in unpopulatedCourses:
                print(course)
            if not unpopulatedCourses:
                print("No unpopulated courses in this department")

    def printMultiSectionCourses(self):

        for department in self.departments:
            print("\nDepartment: " + department.dname)
            multiSectionCourses = department.getMultipleSectionCourses()

            for course in multiSectionCourses:
                print(course)

            if not multiSectionCourses:
                print("No multi-section course in this department")

    def printTopCourses(self):
        for department in self.departments:
            print(f"\nDepartment: {department.dname}")

            topCoursesList = department.getTopCourses()

            for course in topCoursesList:
                print(course)
