from Course import Course

class LabCourse(Course):
    def __init__(self, ccode, cname):
        super().__init__(ccode, cname)
        self.labSections = {}

    def addLabSection(self, labNo, capacity, registeredStudents, instructor):
        self.labSections[labNo] = (instructor, int(capacity), int(registeredStudents))

    def getLabCapacity(self):
        total = 0
        for lab in self.labSections:
            total += self.labSections[lab][1]
        return total

    def __str__(self):
        sections_str = "\n".join([f"{section}: {self.sections[section][0]}" for section in self.sections])
        labs_str = "\n".join([f"{lab}: {self.labSections[lab][0]}" for lab in self.labSections])
        return (f"Course Code: {self.ccode}\n"
                f"Course Name: {self.cname}\n"
                f"Sections: \n{sections_str}\n"
                f"Total Section Capacity: {self.getTotalCapacity()}\n"
                f"Total Section Registered: {self.getTotalRegistered()}\n"
                f"Labs: \n{labs_str}\n"
                f"Total Lab Capacity: {self.getLabCapacity()}\n")

if __name__=="__main__":
    course = LabCourse(22,"CNG 445")
    # Add lab sections with lab number, capacity, number of registered students, and instructor name
    course.addLabSection("Lab1", 30, 25, "Dr. Smith")
    course.addLabSection("Lab2", 25, 20, "Dr. Johnson")
    course.addLabSection("Lab3", 35, 30, "Dr. Williams")

    # Test getLabCapacity method
    print("Total Lab Capacity:", course.getLabCapacity())  # Expected output: 90

    # Test __str__ method
    print(course)