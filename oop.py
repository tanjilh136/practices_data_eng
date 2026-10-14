class Employee:
    raise_amount=1.04
    num_of_emps = 0
    def __init__(self,first_name,last_name,pay):
        self.first_name=first_name
        self.last_name=last_name
        self.pay=pay
        self.email= first_name + '.' + last_name + '@otivexlabs.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first_name} {self.last_name}"
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#     def display(self):
#         return f"Name: {self.fullname()} | Email: {self.email} | Salary: {self.pay}"

#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount

#     @classmethod
#     def from_string(cls, emp_str):
#         first,last,pay = emp_str.split('-')
#         return cls(first,last,pay)

#     @staticmethod
#     def is_workday(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         return True

# class Developer(Employee):
#     def __init__(self,first_name,last_name,pay,prog_lang):
#         super().__init__(first_name,last_name,pay)
#         self.prog_lang = prog_lang

# class Manager(Employee):
#     def __init__(self,first_name,last_name,pay,employees=None):
#         super().__init__(first_name,last_name,pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees

#     def add_emp(self,emp):
#         if emp not in self.employees:
#             self.employees.append(emp)

#     def remove_emp(self,emp):
#         if emp in self.employees:
#             self.employees.remove(emp)

#     def print_emps(self):
#         for emp in self.employees:
#             print('-->',emp.fullname())

emp1 = Employee('Tanjil','Hasan',1500)
#emp2 = Employee.from_string('Nusrat-Jahan-1700')

print(emp1.first_name)
print(emp1.email)
print(emp1.fullname())

# emp1.raise_amount = 1.05
# print(emp1.__dict__)

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.display())
# print(f"Total number of employees: {Employee.num_of_emps}")

# import datetime
# my_date = datetime.date(2024, 6, 15)
# print(Employee.is_workday(my_date))

# dev_1 = Developer('iyaan','Hasan',3500,'Python'     )
# #print(help(Developer))

# mgr_1 = Manager('Tanjil','Hasan',5000,[dev_1])
# print(mgr_1.print_emps()) 