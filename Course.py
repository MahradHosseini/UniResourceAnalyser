class Course:
    def __init__(self, ccode, cname):
        self.ccode = ccode
        self.cname = cname
        self.sections = {}

    def addSection(self, sectionNo, capacity, registeredStudents, instructor):
        # sectionNo is the key, and values are stored in a tuple format
        self.sections[sectionNo] = (instructor, capacity, registeredStudents)

    def getTotalCapacity(self):
        total = 0
        for section in self.sections:
            total += self.sections[section][1] # Index 1 is capacity

        return total

    def getTotalRegistered(self):
        total = 0
        for section in self.sections:
            total += self.sections[section][2] # Index 2 is registered students
        return total

    def __str__(self):
        # Creating a string of sections, joining them with a new line (\n)
        sections_str = "\n".join([f"{section}: {self.sections[section][0]}" for section in self.sections])

        # Returning a string with all the course details
        return (f"Course Code: {self.ccode}\n"
                f"Course Name: {self.cname}\n"
                f"Sections: \n{sections_str}\n"
                f"Total Capacity: {self.getTotalCapacity()}\n"
                f"Total Registered: {self.getTotalRegistered()}\n")
