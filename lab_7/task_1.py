class Employee:
    def __init__(self, emp_number, emp_name, cnic, contact_phone, contact_address):
        self.emp_number = emp_number
        self.emp_name = emp_name
        self.cnic = cnic
        self.contact_phone = contact_phone
        self.contact_address = contact_address


class SalariedEmployee(Employee):
    def __init__(self, emp_number, emp_name, cnic, contact_phone, contact_address, weekly_salary):
        super().__init__(emp_number, emp_name, cnic, contact_phone, contact_address)
        self.weekly_salary = weekly_salary

    def calculate_pay(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, emp_number, emp_name, cnic, contact_phone, contact_address, hours_worked, rate_per_hour):
        super().__init__(emp_number, emp_name, cnic, contact_phone, contact_address)
        self.hours_worked = hours_worked
        self.rate_per_hour = rate_per_hour

    def calculate_pay(self):
        if self.hours_worked <= 40:
            return self.hours_worked * self.rate_per_hour
        else:
            regular_pay = 40 * self.rate_per_hour
            overtime_pay = (self.hours_worked - 40) * (1.5 * self.rate_per_hour)
            return regular_pay + overtime_pay
    

class Payroll:
    def __init__(self):
        self.Employee = []

    def add(self,employee):
        self.Employee.append(employee)

    def calculate_total_payroll(self):
        total_payroll = 0
        for employee in self.Employee:
            total_payroll += employee.calculate_pay()
        return total_payroll
    
    def __str__(self):
        for i in range(len(self.Employee)):
            return f"{self.Employee[i]}"
def main():
    payroll = Payroll()
    a = (HourlyEmployee("1","Kashaf","3108-6478632","0378-88736765","Johar Town Lahore",50,80))
    b = (SalariedEmployee("1","Kashaf","3108-6478632","0378-88736765","Johar Town Lahore",8000))
    payroll.add(a)
    payroll.add(b)
    print(payroll)

    



    
main()