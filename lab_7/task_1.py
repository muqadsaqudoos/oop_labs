class Employee:
    def __init__(self,employee_no,name,cnic_no,phone,address):
        self.employeeNo = employee_no
        self.name = name
        self.cnicNo = cnic_no
        self.phoneNo = phone
        self.address = address

    def __str__(self):
        a = ""
        a += f"\n{str(self.employeeNo)} "
        a += f" {str(self.name)} "
        a += f" {str(self.cnicNo)} "
        a += f" {str(self.phoneNo)} " 
        a += f" {str(self.address)} "
        return a
    
class Salaried(Employee):
    def __init__(self,employee_no,name,cnic_no,phone,address,week_salary):
        super().__init__(employee_no,name,cnic_no,phone,address)
        self.weekSalary = week_salary

    def calculatePay(self):
        return self.weekSalary
    
    def __str__(self):
        b = ""
        b += super().__str__()
        b += f"{str(self.weekSalary)}"
        return b
    
class Hourly(Employee):
    def __init__(self, employee_no, name, cnic_no, phone, address,paid_for_each_hour,hour_worked):
        super().__init__(employee_no, name, cnic_no, phone, address)
        self.paidForEachHour = paid_for_each_hour
        self.hourWorked = hour_worked

    def calculatePay(self):
        if self.hourWorked<=40:
            return (self.hourWorked*self.paidForEachHour)
        else:
            overTimeHours = self.hourWorked-40
            overTimePay = (self.paidForEachHour*40)+(1.5*overTimeHours*self.paidForEachHour)
            return overTimePay
        
    def __str__(self):
        c = ""
        c += super().__str__()
        c += f"{str(self.paidForEachHour)}"
        c += f"{str(self.hourWorked)}"
        return c
    
class Commission(Employee):
    def __init__(self, employee_no, name, cnic_no, phone, address,sales_amount):
        super().__init__(employee_no, name, cnic_no, phone, address)
        self.salesAmount = sales_amount

    def calculatePay(self):
        return (80/100)*self.salesAmount
    
    def __str__(self):
        d = ""
        d +=  super().__str__()
        d += str(self.salesAmount)
        return d

class Payroll:
    def __init__(self):
        self.Employee = []

    def add(self,employee):
        self.Employee.append(employee)

    def totalAmount(self):
        total = 0
        for employee in self.Employee:
            total += employee.calculatePay()
        return total
    
    def __str__(self):
        e = ""
        for employee in self.Employee:
            e += f"{str(employee)}"
        return e
        
            
    
def main():
    payroll = Payroll()
    employee1 = Salaried("24","Kashaf","31301-0000000000","0300-11111111","johar Town,Lahore",5000)
    employee2 = Hourly("25","Hamna","31301-222222222","0300-55555555","G1,Lhaore",15,45)
    employee3 = Hourly("26","Tehreem","31301-555554444","0300-99999999","Township,Lhaore",15,35)
    employee4 = Commission("27","Rabbiya","31301-333888999","0300-000555773","DHA,Lhaore",15000)
    employee5 = Salaried("29","Muqadsa","31301-27795555","0300-2675183","Gulburg,Lhaore",7000)
    payroll.add(employee1)
    payroll.add(employee2)
    payroll.add(employee3)
    payroll.add(employee4)
    payroll.add(employee5)
    print(payroll)
    total = payroll.totalAmount()
    print(total)

main()





