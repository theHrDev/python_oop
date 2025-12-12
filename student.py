class Student:
    def __init__(self,name,age ,grades=[]):
        self.name = name
        self.age = age
        self.grades = grades
        # self.average_grade = average_grade
        
        
    def get_average(self):
        total_grade = 0
        for grade in self.grades:
            total_grade += grade
            lenght = len(grade)
            
            
        average_grade =total_grade / lenght
        self.average_grade = average_grade
        
        return f"Your average score is {average_grade}"
    
    
    def is_promoted(self):
        if self.average_grade < 50:
            return "Your average score is below 50, you are to repeat this class"
        
        else:
            return "You are promoted"
        
        
    
name = input("Enter Your name: ")    
age = int(input("Enter Your age: "))
grades = [90,34,56,75]    
    
studen = Student(name=name,grades=grades, age=age)
studen.get_average()
