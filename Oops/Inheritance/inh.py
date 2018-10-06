from teacher import Teacher

t=Teacher()

t.setaddress('HGP')
t.setid(100)
t.setname('Sujoy Sinha')
t.setsalary(5000)

print('Address: ', t.getaddress())
print('Id: ', t.getid())
print('Name: ', t.getname())
print('Salary: ', t.getsalary())