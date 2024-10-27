from Department import Department
from Course import Course
import re

from LabCourse import LabCourse


class University:
    def __init__(self,uname,ubranch):
        self.uname = uname
        self.ubranch = ubranch
        self.departments = []
    def loadUniversity(self,departmentsFilename,coursesFilename):
        try:
            file = open(departmentsFilename,"r")
        except IOError:
            print("File could not be opened")
            exit(1)
        file_departments = file.readlines()[1:] # Skip the first line
        for i in range(len(file_departments)):
            #separating department name,shortnamen and code
            splited_departments = re.split(",",file_departments[i].strip())
            self.addDepartment(splited_departments[2], splited_departments[1], splited_departments[0])

        try:
            file = open(coursesFilename,"r")
        except IOError:
            print("File could not be opened")
            exit(1)
        file_courses = file.readlines()[1:]  # Skip the first line
        for i in range(len(file_courses)):
            # separating courses name,code, etc.
            splited_courses = re.split(",", file_courses[i].strip())
            #checking if the course code is in the following form CNG 445
            if re.match(r"^\w{3,4}\s\d{3,4}$",splited_courses[1]):
                # creating a new course object
                self.addCourseToDepartment(splited_courses)

    def addDepartment(self,dname,dshortname,dcode):
        # creating a new department object
        new_department = Department(dname, dshortname, dcode)
        # adding the new object to the departments list
        self.departments.append(new_department)

    def addCourseToDepartment(self,courseArray):
        #courseArray indexes : 0.Department code, 1.course code, 2.course name, 3.instructor
        #                     4.section, 5.capacity, 6.registered students
        for department in self.departments:
            #finding the right department to add the course through the department code
            if department.decode == courseArray[0]:
                #checking if the course already exist in the courses and retrieving it
                existing_course = next((course for course in department.courses if course.ccode == courseArray[1]), None)
                #if course doesn't exist add new course
                if not existing_course:
                    #add section course
                    if re.match(r"S\d+", courseArray[4]):
                        department.addCourse(courseArray[1], courseArray[2])
                        existing_course = department.courses[-1]
                    #add lab course
                    else:
                        department.addLabCourse(courseArray[1],courseArray[2])
                        existing_course = department.courses[-1]
                #checking if the course code matches the pattern
                if re.match(r"S\d+", courseArray[4]):  # If section starts with "S", it's a regular section
                    existing_course.addSection(courseArray[4], courseArray[5], courseArray[6], courseArray[3])

                else:  # Otherwise, it's a lab section
                    existing_course.addLabSection(courseArray[4], courseArray[5], courseArray[6], courseArray[3])

if __name__ == "__main__":
    university = University("METU","NCC")
    university.loadUniversity("departments.txt","courses.txt")
    for department in university.departments:
        for course in department.courses:
            print(course)