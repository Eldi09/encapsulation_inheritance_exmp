class Student:
    def __init__(self, name, id, enllorment_date):
        self.name = name
        self.id = id
        self.enllorment_date = enllorment_date
        self.__grades = []
    
    def add_grades(self, course_name, grade):
        for i in self.__grades:
            if i[0] == course_name:
                print("You already have a grade in this course")
                return self
        self.__grades.append((course_name, grade))
        print(self.__grades)
        return self
    
    def get_grade(self, course_name):
        for i in self.__grades:
            if i[0] == course_name:
                print(f"Your grade in {course_name} is {i[1]}")
                return self
        print("This course does not exist")
        return self

    def get_avg_grade(self):
        sum = 0
        for i in self.__grades:
            sum += i[1]
        avg_grade = sum / len(self.__grades)
        print(f"Your average grade is {avg_grade}")
        return self

john = Student("John Smith", 123456, "16.03.2022")
john.add_grades("Math", 95).add_grades("Biology", 90)
john.get_grade("Science")
john.get_avg_grade()
