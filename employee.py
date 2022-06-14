#  File: employee.py
#  Description: Creates class definitions for various types of employees in a company that inherit various characteristics from one another
#  Student Name: Sean Thomas
#  Student UT EID: sft372
#  Partner Name: Emily Wang
#  Partner UT EID: ew6985
#  Course Name: CS 313E
#  Unique Number: 86439
#  Date Created: 06/13/2022
#  Date Last Modified: 06/13/2022

import sys

class Employee():
    """The base class for all other class which has a basic salary"""

    def __init__(self, **kwargs):
        """Initializes the employee with a name, id, and salary"""
        self.name = kwargs.get("name")
        self.id = kwargs.get("id")
        self.salary = kwargs.get("salary")
        
    
    def __str__(self):
        """Return a string representation of the Employee with their name and salary""" 
        return self.name + "'s salary is " + str(self.salary)


############################################################
############################################################
################################################y############

class Permanent_Employee(Employee):
    """A subclass of Employee who can receive benefits and whose actual salary depends on the benefits they choose"""
    def __init__(self, **kwargs):
        "Initializes the object with the attributes of Employee along side a list of benefits"""
        super().__init__(**kwargs)
        self.benefits = kwargs.get("benefits")
        


    def cal_salary(self):
        """Determine the salary based on the chosen benefits, the more benefits the employee chooses, the lower the salary"""
        if self.benefits == ["health_insurance"]:
            return self.salary * 0.9
        elif self.benefits == ["retirement"]:
            return self.salary * 0.8
        elif self.benefits == ["retirement", "health_insurance"]:
            return self.salary * 0.7
        else:
            return self.salary
            



    def __str__(self):
        """Return a string representation of the employee with their name and the salary calculated based on their chosen benefits"""
        return self.name + "'s salary is " + str(self.cal_salary())


############################################################
############################################################
############################################################

class Manager(Employee):
    """A subclass of employee that receives both a salary and a bonus""" 
    def __init__(self, **kwargs):
        "Initializes the object with the attributes of Employee along side a bonus"""
        super().__init__(**kwargs)
        self.bonus = kwargs.get("bonus")
        
    def cal_salary(self):
        """Gets a total salary which is the combination of the Manager's salary and bonuses"""
        return self.salary + self.bonus

    def __str__(self):
        """Return a string representation of the employee with their name and their total salary with their bonus"""
        return self.name + "'s salary is " + str(self.cal_salary())


############################################################
############################################################
############################################################
class Temporary_Employee(Employee):
    """A subclass of employee that does not work enough to recieve benefits, and is paid depending on their worked hours"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hours = kwargs.get("hours")

    def cal_salary(self):
        """Gets a total salary depending on the number of hours worked"""
        return self.salary * self.hours


    def __str__(self): 
        """Returns a string representation of the employee with their name and calculated salary"""
        return self.name + "'s salary is " + str(self.cal_salary())



############################################################
############################################################
############################################################


class Consultant(Temporary_Employee):
    """A subclass of Temporary Employee that also travels and is paid money depending on their travel"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.travel = kwargs.get("travel")
        


    def cal_salary(self):
        """Gets a total salary that adds the travel pay on top of the Temp. employee pay"""
        return super().cal_salary() + 1000 * self.travel
    
    def __str__(self):
        """Returns a string representation of the employee with their name and calculated salary including travel pay"""
        return self.name + "'s salary is " + str(self.cal_salary())


    

############################################################
############################################################
############################################################


class Consultant_Manager(Manager, Consultant):
    """A subclass of the Manager and Consultant positions that recieves both the travel pay and bonuses"""
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        Consultant.__init__(self, **kwargs)


    def cal_salary(self):
        """Gets a total salary that combines both the Consultant and Manager pay"""
        return Consultant.cal_salary(self) + self.bonus
        

    def __str__(self):
        """Returns a string representation of the employee with their name and calculated salary"""
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
