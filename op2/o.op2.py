class Employee:

    def __init__(self):
        print("Employee created.")

    def __del__(self):
        print("destructor destroyed the employee")

obj = Employee()
del obj