class employee:
    def __init__(self):
        self.empname = "Sreehari"
        self.empID = 102533
        self.empSal =  25000


    def location(self,cityname):
        print(f"Employee Location is : {cityname}")

empobj = employee()
print(f"Employee Name is : {empobj.empname}")

empobj.location("Bangalore")

print(type(empobj))
print(type(empobj.empSal))