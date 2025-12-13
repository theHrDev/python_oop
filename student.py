class Student:
    # average_grade = 0
    def __init__(self,name,age,grades):
        self.name = name
        self.age = age
        self.grades = grades
        # self.average_grade 
        
        
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
        
    def is_promoted(self,pass_mark = 50):
        return self.get_average() >= pass_mark
        
    
def student_calc():
        
    name = input("Enter Your name: ")    
    age = int(input("Enter Your age: "))
    raw = input("Enter grades (comma-separated): ")
    grades = [int(g.strip()) for g in raw.split(",")]

    student = Student(name, age, grades)

    # grades = [90,34,56,75]    
        
    student = Student(name=name,grades=grades, age=age)
    average = student.get_average()
    print(f"Average score: {average}")

    if student.is_promoted():
        print("You are promoted")
    else:
        print("You must repeat the class")
        
student_calc()


