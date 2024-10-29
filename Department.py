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
        return [course for course in self.courses if course.getTotalRegistered() < 5]

    def getMultipleSectionCourses(self):
        multiSectionCourses = []
        for course in self.courses:
            numOfSections = len(course.sections.items())
            numOfLabs = 0
            if isinstance(course, LabCourse):
                numOfLabs = len(course.labSections.items())

            if numOfSections > 1 or numOfLabs > 1:
                multiSectionCourses.append(course)

        return multiSectionCourses

    def getTopCourses(self):
        maxRegistered = 0
        topCoursesList = []

        for course in self.courses:
            totalRegistered = course.getTotalRegistered()
            if totalRegistered > maxRegistered:
                maxRegistered = totalRegistered
                topCoursesList = [course]  # Starting a new list
            elif totalRegistered == maxRegistered:
                topCoursesList.append(course)

        return topCoursesList

    def __str__(self):
        return "Department name: " + self.dname + " Department code: " + str(self.dcode)
