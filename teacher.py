class Teacher:
    def __init__(self,name,lesson):
        self.name = name
        self.lesson = lesson
    def teach(self):
        print(f"{self.name} is teaching..")
    def rest(self):
        print(f"{self.name} is resting..")