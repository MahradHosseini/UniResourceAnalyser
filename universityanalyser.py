from Course import *

# This file needs to be changed according to the manual,
# It's just a test dummy for now
# But please don't erase them unless you want to implement them according to the manual

if __name__ == "__main__":
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

            # These lines need to be inside the loop
            if courseCode not in courses:
                course = Course(courseCode, courseName)
                courses[courseCode] = course
            else:
                course = courses[courseCode]

            course.addSection(section, capacity, registeredStudents, instructor)

    for courseCode, course in courses.items():
        print(course)
