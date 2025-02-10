class student:
  grade = 5 
  name ="yes"
  def introduction(self):
        print("Hi im a student")
  def details(self):
        print("My name is", self.name)
        print("I study in grade", self.grade)
ob=student()
ob.introduction()
ob.details()