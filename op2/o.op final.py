class square:
      def __init__(self,side):
          self.side = side
          
      def area(self):
            print("My area is:", self.side**2)
            
class Circle:
      def __init__(self, radius):
                     self.radius = radius

      def __init__(self, radius):
             self.radius = radius

      def area(self):
          print("MY area is", 3.14 *self.radius*self.radius) 
class trapezium:
       def __init__(self, base1,base2, height):
              self.base1 = base1
              self.base2 = base2
              self.height = height

       def area(self):
              print("My area is", 0.5 , (self.base1 + self.base2) * self.height)

side_length = int(input("Enter the side length of the square"))
radius_length = int(input("Enter the radius of the circle"))
base1 = int(input("Enter the radius of the trapezium"))
base2 = int(input("enter the second base of the trapezium"))
height = int(input("Enter the height of the trapezium"))
osquare = square(side_length)
ocircle = Circle(radius_length)
otrapezoid=trapezium(base1, base2, height)
for shape in (osquare, ocircle, otrapezoid):
       shape.area()