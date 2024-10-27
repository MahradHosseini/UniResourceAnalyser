from Course import *
from LabCourse import *


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
    for courseCode, course in LoadCourses().items():
        print(course)
