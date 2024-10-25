class Course:

    def __init__(self, ccode, cname):
        self.ccode = ccode
        self.cname = cname
        self.sections = {}

    def addSection(self, sectionNo, capacity, registeredStudents, instructor):
        self.sections[sectionNo] = (instructor, capacity, registeredStudents)

    def getTotalCapacity(self):
        total = 0
        for section in self.sections:
            total += self.sections[section][1]

        return total

    def getTotalRegistered(self):
        total = 0
        for section in self.sections:
            total += self.sections[section][2]
        return total

    def __str__(self):
        sections_str = "\n".join([f"{section}: {self.sections[section][0]}" for section in self.sections])
        return (f"Course Code: {self.ccode}\n"
                f"Course Name: {self.cname}\n"
                f"Sections: \n{sections_str}\n"
                f"Total Capacity: {self.getTotalCapacity()}\n"
                f"Total Registered: {self.getTotalRegistered()}\n")