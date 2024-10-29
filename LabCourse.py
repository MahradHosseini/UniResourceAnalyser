from Course import Course


class LabCourse(Course):
    def __init__(self, ccode, cname):
        super().__init__(ccode, cname)
        self.labSections = {}

    def addLabSection(self, labNo, capacity, registeredStudents, instructor):
        # labNo is the key, and values are stored in a tuple format
        self.labSections[labNo] = (instructor, capacity, registeredStudents)

    def getLabCapacity(self):
        total = 0
        for lab in self.labSections:
            total += self.labSections[lab][1] # Index 1 is the lab capacity
        return total

    def __str__(self):
        # Creating a string of sections, joining them with a new line (\n)
        sections_str = "\n".join([f"{section}: {self.sections[section][0]}" for section in self.sections])

        # Doing the same thing for the lab sections
        labs_str = "\n".join([f"{lab}: {self.labSections[lab][0]}" for lab in self.labSections])

        # Returning a string with all the course details
        return (f"Course Code: {self.ccode}\n"
                f"Course Name: {self.cname}\n"
                f"Sections: \n{sections_str}\n"
                f"Total Section Capacity: {self.getTotalCapacity()}\n"
                f"Total Section Registered: {self.getTotalRegistered()}\n"
                f"Labs: \n{labs_str}\n"
                f"Total Lab Capacity: {self.getLabCapacity()}\n")

