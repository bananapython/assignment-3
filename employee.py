#  File: employee.py
#  Description: Creates class definitions for various types of employees in a company that inherit various characteristics from one another
#  Student Name: Sean Thomas
#  Student UT EID: sft372

#  Course Name: CS 313E
#  Unique Number: 86439
#  Date Created: 06/13/2022
#  Date Last Modified: 06/13/2022

import sys

class Employee():

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.id = kwargs.get("id")
        self.salary = kwargs.get("salary")
        
    
    def __str__(self):
        return self.name + "'s salary is " + str(self.salary)


############################################################
############################################################
################################################y############

class Permanent_Employee(Employee):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.benefits = kwargs.get("benefits")
        


    def cal_salary(self):
        if self.benefits == ["health_insurance"]:
            return self.salary * 0.9
        elif self.benefits == ["retirement"]:
            return self.salary * 0.8
        elif self.benefits == ["retirement", "health_insurance"]:
            return self.salary * 0.7
        else:
            return self.salary
            



    def __str__(self):
        return self.name + "'s salary is " + str(self.cal_salary())


############################################################
############################################################
############################################################

class Manager(Employee):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bonus = kwargs.get("bonus")
        
    def cal_salary(self):
        return self.salary + self.bonus

    def __str__(self):
        return self.name + "'s salary is " + str(self.cal_salary())


############################################################
############################################################
############################################################
class Temporary_Employee(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hours = kwargs.get("hours")

    def cal_salary(self):
        return self.salary * self.hours


    def __str__(self): 
       return self.name + "'s salary is " + str(self.cal_salary())



############################################################
############################################################
############################################################


class Consultant(Temporary_Employee):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.travel = kwargs.get("travel")
        


    def cal_salary(self):
        return super().cal_salary() + 1000 * self.travel
    
    def __str__(self):
        return self.name + "'s salary is " + str(self.cal_salary())


    

############################################################
############################################################
############################################################


class Consultant_Manager(Manager, Consultant):
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        Consultant.__init__(self, **kwargs)


    def cal_salary(self):
        return Consultant.cal_salary(self) + self.bonus
        

    def __str__(self):
        return self.name + "'s salary is " + str(self.cal_salary())



############################################################
############################################################
############################################################



###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():

    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")


if __name__ == "__main__":
  main()

