class Student:
    def __init__(self,name,roll,department,marks):
        self.name = name
        self.roll = roll
        self.department = department
        self.marks = marks
    def give_remark(self):
        if self.marks >= 90:
            print(f"{self.name} you got A+")
        elif self.marks >= 70:
            print(f"{self.name} you got A")
        elif self.marks >= 60:
            print(f"{self.name} you got B+")
        elif self.marks >= 50:
            print(f"{self.name} you got B")
        elif self.marks >= 40:
            print(f"{self.name} you got C")
        else:
            print(f"{self.name} you got F")


student1 = Student('Abhilock',4,'AIDS',100)
student2 = Student('Swarna',1,'AIDS',90)
student3 = Student('Chandradip',5,'AIDS',80)
student4 = Student('Bittu',10,'AIDS',75)
student5 = Student('Dip',7,'AIDS',30)
Student.give_remark(student1)
Student.give_remark(student2)
Student.give_remark(student3)
Student.give_remark(student4)
Student.give_remark(student5)