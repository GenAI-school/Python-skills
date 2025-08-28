# Python-skills
This repository is to work on learning python language for Gen AI

# Creating Class in python
    class employee:

# Defining constructor inside a class
    def _init_(self)
        self.empName = "Sreehari"
        self.empID = 102533
        self.empSalary = 25000

# Creating object for a class
    empobj = employee()

# Accessing attributes of a class
    empobj.empname
    print(f"Employee Name is : {empobj.empname}")

# Creating method inside a class
    def location(self,cityname):
        
        print(f"Employee Location is : {cityname}")

# Accessing method of a class
    empobj.location("Bangalore")

# Checking the data type of variable
     print(type(empobj))
     print(type(empobj.empSal))

# Importing a class
    from app02 import chatbook
# Encapsulation
To hide the sensitive data of a class encapsulation is used

    class employee:
        def __init__(self):
            self.__company = "TCS"

To acess hidden attribute from other calss,we have to use below format
    
    empobj1 = employee()
    print(f"Employee company is : {empobj1._employee__company}")

#  Creating Static methods and getter, setter methods in a class

    class chatbook:
    __bankbalance = 0
    def __init__(self):
        self.__name = "communication platform"
        chatbook.__bankbalance+=10000

    @staticmethod
    def get_bal():
        return chatbook.__bankbalance
    
    @staticmethod
    def set_bal(amount):
        chatbook.__bankbalance = amount 

# Accessing static and getter,setter methods in a class

Static methods or variables can be accessed using class name,no need to create object to access static members of a class

    from app02 import chatbook

    print(chatbook._chatbook__bankbalance)
    chatbook.set_bal(50000)
    print(chatbook.get_bal())