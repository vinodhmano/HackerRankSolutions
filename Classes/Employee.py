class Employee:

  raise_percentage = 12

  def __init__(self, first_name, last_name, age):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
  
  def set_compensation(self, pay):
    self.pay = pay

  def get_name(self):
    return '{} {}'.format(self.first_name, self.last_name)
  
  def get_employee_details(self):
    return  "Employee Name : {} \nEmployee Age: {} \nEmployee Pay: {}".format(self.get_name(), self.age, self.pay)

  def give_raise(self):
    if(Employee.raise_percentage > 0):
      self.pay = self.pay + (self.pay * (Employee.raise_percentage / 100))

  @classmethod
  def set_raise_percentage(cls, percentage):
    cls.raise_percentage = percentage

  @classmethod
  def get_raise_percentage(cls):
    
    return cls.raise_percentage



if __name__ == '__main__':
  e1 = Employee("Vinodhraj", "Manoharan", 23)
  e1.set_compensation(161000)
  print(e1.get_employee_details())
  Employee.set_raise_percentage(5)
  e1.give_raise()
  print(e1.get_employee_details())
  
  
