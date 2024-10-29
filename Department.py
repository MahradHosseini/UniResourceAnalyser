from Course import Course
from LabCourse import LabCourse


class Department:
    def __init__(self, dname="?", dshortname="?", dcode=0):
        self.dname = dname
        self.dshortname = dshortname
        self.dcode = dcode
        self.courses = []

    def addCourse(self, ccode, cname, isLabCourse):
        if isLabCourse:
            course = LabCourse(ccode, cname)
        else:
            course = Course(ccode, cname)
        self.courses.append(course)

    def getLabCourses(self):
        return [course for course in self.courses if isinstance(course, LabCourse)]

    def getTotalLabCapacity(self):
        totalCapacity = 0
        for course in self.getLabCourses():
            totalCapacity += course.getTotalCapacity()
        return totalCapacity

    def getUnpopulatedCourses(self):
        # Returning a list of course objects which have less than 5 students enrolled
        return [course for course in self.courses if course.getTotalRegistered() < 5]

    def getMultipleSectionCourses(self):
        multiSectionCourses = []
        for course in self.courses:
            # Counting the number of sections in each course
            numOfSections = len(course.sections.items())
            numOfLabs = 0

            # If the object is a LabCourse, then count the number of lab sections
            if isinstance(course, LabCourse):
                numOfLabs = len(course.labSections.items())

            # If a course has more than 1 section or more than 1 lab section, add it to multi-section course list
            if numOfSections > 1 or numOfLabs > 1:
                multiSectionCourses.append(course)

        return multiSectionCourses

    def getTopCourses(self):
        maxRegistered = 0
        topCoursesList = []

        for course in self.courses:
            # Counting the total registered students in a course
            totalRegistered = course.getTotalRegistered()

            # If it's bigger than the current top course, set this as the max number and initiate a new list with this
            # course at the top
            if totalRegistered > maxRegistered:
                maxRegistered = totalRegistered
                topCoursesList = [course]  # Starting a new list

            # If this course is as big as the current top course, append it to the top course list
            elif totalRegistered == maxRegistered:
                topCoursesList.append(course)

        return topCoursesList

    def __str__(self):
        return "Department name: " + self.dname + " Department code: " + str(self.dcode)
