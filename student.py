class Student:
    def __init__(self,name,studentNumber) :
        self.name = name
        self.studentNumber=studentNumber
    def doHomework(self):
        print(f"{self.name} is doing homework..")
    def study(self):
        print(f"{self.name} is studying..")