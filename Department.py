from Course import Course
from LabCourse import LabCourse


class Department:
    def __init__(self,dname="?", dshortname = "?", dcode =0):
        self.dname = dname
        self.dshortname = dshortname
        self.decode = dcode
        self.courses = []

    def addCourse(self,ccode,cname,isLabCourse):
        if isLabCourse :
            course = LabCourse(ccode, cname)
        else:
            course = Course(ccode,cname)
        self.courses.append(course)

    def getLabCourses(self):
        return [course for course in self.courses if isinstance(course,LabCourse)]

    def getTotalLabCapacity(self):
        totalCapacity = 0
        for course in self.getLabCourses():
            totalCapacity+=course.getTotalCapacity()

    def getUnpopulatedCourses(self):
        return [course for course in self.courses if course.getTotalCapacity() < 5]

    def getMultipleSectionCourses(self):
        # get lab courses that have lab sections
        lab_courses = [lab_course for lab_course in self.getLabCourses() if bool(lab_course.labSections)]
        # get regular courses that have sections
        regular_courses = [course for course in self.courses if bool(course.sections)]
        # combine both lists and return it as one list
        return lab_courses + regular_courses

    def getTopCourses(self):
        courseWithCapacity = []
        #combining the course and the capacity in 2d array
        for course in self.courses:
            courseWithCapacity.append([course,course.getTotalCapacity()])
        #sorting the 2d array according to capacity
        sorted_courses = sorted(courseWithCapacity,key=lambda x: x[1], reverse=True)
        #printing the courses in descending order
        for course,capacity in sorted_courses:
            print(course)

    def __str__(self):
        return "Department name: "+ self.dname + " Department code: "+ str(self.decode)
