class employee:
    count = 0
    nums_of_init = 0
    name ='me'
    def __init__(self ,first, last, email,obj=None):
        self.first = first
        self.last = last
        self.email = email
        if obj is None:
            self.obj = []
        else:
            self.obj = obj
        employee.nums_of_init+=1

    def fullname(not_self):
        return not_self.first ,not_self.last
    @classmethod
    def change_name(cls, value):
        cls.name = value
        return cls.name 
    
    def Count(self, value):
        for i in self.obj:
            if i == value:
                self.count+=1
        return self.count
    @staticmethod
    def work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    #@property
    def __add__(self, other):
        if other:
            return self.first + ' ' + other.first
        return NotImplemented
    def __str__(self):
        return self.first + "|" +self.last
    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.email})"
    @property
    def full_names(self):
        # first, last = name.split(" ")
        # self.first = first
        # self.last =  last
        return f"{self.first} | {self.last}"
    @full_names.setter
    def f(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

emp = employee(last='Admin', first='Ebuka',email='s',obj=[1,2,3,5])
emp1 = employee(first='Admin', last='Ebuka',email='s',obj=[1,2,3,5])

i=6
print(emp.full_names) 
emp.f= "Corey Me"
print(emp.full_names) 

print(emp+emp1)
# print(employee.first_names(emp,"ME YOU",emp1))
# print(emp.first)
# import datetime
# date = datetime.date(2023,7,28)
# print(type(date))
# print(employee.work_day([2023-7-28]))
# print(employee.change_name('another_me'))
# print(employee.nums_of_init)
# print(emp.fullname())
#print(emp.email)
# print(dir([]))
# print(employee('Admin', 'Ebuka','s',obj=[1,2,3,5]).Count(1))
print('p',emp.Count(1))
s=[]