# Justin Xu
# Assignment 10.1
# The purpose of this assingment is to create and implement my own class based on a real-world object.

import argparse
import datetime

# Creating Class
class Student:
# Class Variable
    school = 'UCSC'
# Defining data variables name, and date of birth
    def __init__(self, name, dob):
        self.__dob = dob
        self.__name = name
# Sets the date of birth
    def set_dob(self, x):
        self.__dob = x
# Gets the date of birth 
    def get_dob(self):
        x = self.__dob
        return x
# Sets the name
    def set_name(self, x):
        self.__name = x
# Gets the name
    def get_name(self):
        x = self.__name
        return x
# Prints the name, school, and date of brith of the student
    def get_student_detials(self):
        x = print(f'{self.__name}, {self.school}, {self.__dob}')
        return x
# Does simple arithmetics depends on what the user chooses. 
    def do_math(self, Mtype, x, y):
        if Mtype == 'Addition' or Mtype == 'addition':
            sum = x + y
            print(f'The answer is: {sum}')
            return sum
        elif Mtype == 'Subtraction' or Mtype == 'subtraction':
            remainder = x - y
            print(f'The answer is: {remainder}')
            return remainder
        elif Mtype == 'Multiply' or Mtype == 'multiply':
            product = x * y
            print(f'The answer is: {product}')
            return product
        elif Mtype == 'Division' or Mtype == 'division':
            quotient = x / y
            print(f'The answer is: {quotient}')
            return quotient
# Gets the age of the students based on what year is entered.
    def find_age(self): 
        self.__dob = self.__dob.split('-')
        ogbyear = self.__dob[0]
        byear = int(ogbyear)
        date = datetime.datetime.now()
        year = date.year
        age = year - byear
        print(age)
        return age
# Main funcion with test code
# First creates a student object and then prints the students full details, before running the code the user can additionally choose the type of arithmetic and the two numbers being operated on
# Then the code returns the answer of the operation and returns the age of the student. After that the studnet's date of birth is changed and the age is found again.
def main():
    student1 = Student('Justin', '2003-2-1')
    parser = argparse.ArgumentParser()
    parser.add_argument('--Mtype', help='Sets the operation done to the two inputted numbers', type=str, required=True)
    parser.add_argument('--x', help='Sets the first Number to be operated on', type=int, required=True)
    parser.add_argument('--y', help='Sets the second number to be operated on', type=int, required=True)
    args = parser.parse_args()
    student1.get_student_detials()
    student1.do_math(args.Mtype, args.x, args.y)
    student1.find_age()
    student1.set_dob('1995-2-1')
    student1.find_age()
    
    


if __name__ == '__main__':
    main()