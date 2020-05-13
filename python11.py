# Class and Instance variable

class employee:
    company = 'IT Soft Sol'             #Class Variable

    def __init__(self,name,empid):
        self.name = name                
        self.empid = empid
    def display(self):
        print('Employee Name: ',self.name)
        print('Employee ID: ',self.empid)
        print('Company: ',employee.company)

employee1 = employee('Jim Anderson','ITSS898')
employee1.display()

employee2 = employee('Arthor John','ITSS68')
employee2.display()