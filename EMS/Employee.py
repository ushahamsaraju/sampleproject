import re
#from randompwd import id_generator, get_emp_details
from validations import *
import smtplib
from sub_options import *
#from options import get_emp_details
class cl_Employee():
    def add_employee(self):
        Eid=v.validation_Empno()
        Ename=raw_input("Enter Employee Name:")
        Designation=raw_input("Enter Employee Designation:")
        Deptno=v.validation_deptno()
        Address=raw_input("Enter Employee Address:")
        Salary=v.validation_Salary()
        Email=v.validation_Email()
        Phno=v.validation_Phno()
        f=open("employee.txt","a")
        data="%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n"%(Eid,Ename,Designation,Deptno,Salary,Email,Address,Phno)
        f.write(data)        
        f.close()
        print "You have registered successfully"
        print "*"*30
        print "Please go through below options:"
        print "1.If you want to add one more employee: "
        print "2.If you want go to options of employee: "
        print "3.if you want to exit:"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
        if ch==1:
            e=cl_Employee()
            e.add_employee()
        elif ch==2:
            from sub_options import suboptions
            su= suboptions()
            su.employee_options()
        elif ch==3:
            exit()
        else:
            print "invalid choice, enter a correct choice:"
            return
    def update_employee(self):
        Ename=raw_input("Enter employee old name:")
        new=raw_input("Enter  new name:")
        f = open("employee.txt","r")
        lines=f.readlines()
        for i in range(len(lines)):
            words=lines[i].split("\t")
            if words[1] == Ename:
                lines[i] = lines[i].replace(Ename,new)
                print lines[i]
                break
        else:
            print "Record Not Found"
            return
        f.close()
        with open("employee.txt","w") as f:
            f.write("".join(lines))
            f.close()
            print " Employee details Updated Successfully"
            print "*"*30
        print "Please go through below options:"
        print "1.If you want to update one more employee: "
        print "2.If you want go to options of employee: "
        print "3.if you want to exit:"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
        if ch==1:
            e=cl_Employee()
            e.update_employee()
        elif ch==2:
            from sub_options import suboptions
            su= suboptions()
            su.employee_options()
        elif ch==3:
            exit()
        else:
            print "invalid choice, enter a correct choice:"
            return
    def find_employee(self):
        Eid=raw_input("Enter Employee Number:")
        f=open("employee.txt","r")
        lines=f.readlines()
        for line in lines:
            words=line.split("\t")
            if words[0]==Eid:
                print line
                print "The Employee Data Found Successfully"
                break
        else:
            print "The Data Doesnot found on the Employee number"
        f.close()
        print "*"*30
        print "Please go through below options:"
        print "1.If you want to find one more employee: "
        print "2.If you want go to options of employee: "
        print "3.if you want to exit:"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
        if ch==1:
            e=cl_Employee()
            e.find_employee()
        elif ch==2:
            from sub_options import suboptions
            su= suboptions()
            su.employee_options()
        elif ch==3:
            exit()
        else:
            print "invalid choice, enter a correct choice:"
            return
    def list_employee(self):
        f=open("employee.txt","r")
        lines=f.readlines()
        print "*"*50
        print "The Employees Details the Organization are:"
        print "*"*50
        for line in lines:
            print line
        f.close()
        print "The Details of each and every employee in organization are displayed"
        print "*"*30
        print "Please go through below options:"
        print "1.If you want go to options of employee: "
        print "2.if you want to exit:"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
        if ch==1:
            from sub_options import suboptions
            su= suboptions()
            su.employee_options()
        elif ch==2:
            exit()
        else:
            print "invalid choice, enter a correct choice:"
            return
    def delete_employee(self):
        Eid=raw_input("Enter Employee Number:")
        f=open("employee.txt","r")
        lines=f.readlines()
        for i in range(len(lines)):
            words=lines[i].split("\t")
            if words[0]==Eid:
                print lines[i]
                lines.pop(i)
                f=open("employee.txt","w")
                f.write("".join(lines))
                f.close()
                print "The Employee Record was deleted"
                break
        else:
            print "There is no record on the employee id"
            f.close()
        print "*"*30
        print "Please go through below options:"
        print "1.If you want to delete one more employee: "
        print "2.If you want go to options of employee: "
        print "3.if you want to exit:"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
        if ch==1:
            e=cl_Employee()
            e.delete_employee()
        elif ch==2:
            from sub_options import suboptions
            su= suboptions()
            su.employee_options()
        elif ch==3:
            exit()
        else:
            print "invalid choice, enter a correct choice:"
            return
e=cl_Employee()
#e.add_employee()
#e.update_employee()
#e.find_employee()
#e.list_employee()
#e.delete_employee()
