import re
from randompwd import id_generator,get_emp_details
import smtplib
class employee():
    def add_employee(self):
        Eid=raw_input("Enter Employee Number:")
        while True:
            if Eid in get_emp_details(0):
                print "NUmber Already exists"
                print "Enter a number once again"
            else:
                break
        Ename=raw_input("Enter Employee Name:")
        Designation=raw_input("Enter Employee Designation:")
        Deptno=raw_input("Enter Employee Department Number:")
        flag=True
        while flag:
            try:
                Salary=int(raw_input("Enter Employee Salary:"))
            except Exception as e:
                print "Enter only Integer values"
                continue
            if int(Salary)>0:
                flag=False
            else:
                print "Salary Should be Positive, please enter correctely"
        flag = True
        while flag:
            Email = raw_input("Please Enter Email :")
            if re.search('\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+',Email):
                flag = False
            else:
                print "Invalid Email, Please try again."
        Address=raw_input("Enter Employee Address:")
        flag = True
        while flag:
            try:
                Phno = int(raw_input("Please Enter 10 digit Mobile Number :"))
            except Exception:
                    print "Enter only numbers, Please try again."
                    continue
            if len(str(Phno)) == 10:
                flag = False
            else:
                print "Invalid Phone Number, Please try again."
        f=open("employee.txt","a")
        data="%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n"%(Eid,Ename,Designation,Deptno,Salary,Email,Address,Phno)
        f.write(data)        
        f.close()
        s=raw_input("enter y or n")
        print "If You want to enter one more employee:",s
        if s=='y':
            add_employee()
        else:
            exit()        
e=employee()
e.add_employee()
