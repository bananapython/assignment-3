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
"""The base class for all other class which has a basic salary"""

    def __init__(self, **kwargs):
        self.__name = kwargs.get("name")
        self.__id = kwargs.get("id")
        self.__salary = kwargs.get("salary")
        
    
    def __str__(self):
        return self.__name + "'s salary is " + str(self.__salary)


############################################################
############################################################
################################################y############

class Permanent_Employee(Employee):
"""A subclass of Employee who can receive benefits and whose actual salary depends on the benefits they choose"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__benefits = kwargs.get("benefits")
        


    def cal_salary(self):
        if self.__benefits == ["health_insurance"]:
            return self.__salary * 0.9
        elif self.__benefits == ["retirement"]:
            return self.__salary * 0.8
        else:
            return self.__salary * 0.7



    def __str__(self):
        return self.__name + "'s salary is " + str(self.cal_salary())


############################################################
############################################################
############################################################

class Manager(Employee):
"""A subclass of employee that receives both a salary and a bonus"""    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__bonus = kwargs.get("bonus")
        
    def cal_salary(self):
        return self.__salary + self.__bonus

    def __str__(self):
        return self.__name + "'s salary is " + str(self.cal_salary())


############################################################
############################################################
############################################################
class Temporary_Employee(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__hours = kwargs.get("hours")

    def cal_salary(self):
        return self.__salary * self.__hours


    def __str__(self):
        self.__name + "'s salary is " + str(self.cal_salary())



############################################################
############################################################
############################################################


class Consultant(Temporary_Employee):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__travel = kwargs.get("travel")
        


    def cal_salary(self):
        return super().cal_salary() + 1000 * self.__travel
    
    def __str__(self):
        self.__name + "'s salary is " + str(self.cal_salary())


    

############################################################
############################################################
############################################################


class Consultant_Manager(Manager, Consultant):
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        Consultant().__init__(self, **kwargs)


    def cal_salary(self):
        return Consultant().cal_salary(self) + self.__bonus
        

    def __str__(self):
        self.__name + "'s salary is " + str(self.cal_salary())



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
