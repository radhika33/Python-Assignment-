# question 5:-Python Program to Form a Dictionary from an Object of a Class

class student(object):
    def __init__(self):
        self.name = "Radhika"
        self.rollno = 25
        self.age = 23

    def do_nothing(self):
        pass

student1 = student()
print(student1.__dict__)