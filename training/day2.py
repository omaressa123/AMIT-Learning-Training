class Student:
    counter = 0  
    def __init__(self, name, age, num_courses):
        self.name = name
        self.age = age
        self.num_courses = num_courses
        Student.counter += 1  

    def display(self):
        return f"Name: {self.name}, Age: {self.age}, Number of Enrolled Courses: {self.num_courses}"


student1 = Student("Ali", 20, 5)
student2 =Student("omar",21,6)

print(student1.display())
print(student2.display())

print("Number of students stored:", Student.counter)
