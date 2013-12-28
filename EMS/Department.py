import re
import smtplib
from validations import *
class cl_Dept():
    def add_dept(self):
        Deptno=v.validation_dno()
        Dname=raw_input("Enter Department Name:")
        Loc=raw_input("Enter Department Location:")
        f=open("department.txt","a")
        data="%s\t%s\t%s\t\n"%(Deptno,Dname,Loc)
        f.write(data)        
        f.close()
        print "The record added successfully"
        print "*"*30
        print "Please go through below options:"
        print "1.If you want to add one more Department: "
        print "2.If you want go to options of Department: "
        print "3.if you want to exit:"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
        if ch==1:
            de=cl_Dept()
            de.add_dept()
        elif ch==2:
            from sub_options import suboptions
            su= suboptions()
            su.department_options()
        elif ch==3:
            exit()
        else:
            print "invalid choice, enter a correct choice:"
            return

    def update_dept(self):
        Loc=raw_input("Enter Department location :")
        new=raw_input("Enter  new location:")
        f = open("department.txt","r")
        lines=f.readlines()
        for i in range(len(lines)):
            words=lines[i].split("\t")
            if words[2] == Loc:
                lines[i] = lines[i].replace(Loc,new)
                print lines[i]
                break
        else:
            print "Record Not Found"
            return
        f.close()
        with open("department.txt","w") as f:
            f.write("".join(lines))
            f.close()
            print " Department Location Updated Successfully"
            print "*"*30
        print "Please go through below options:"
        print "1.If you want to update one more department: "
        print "2.If you want go to options of department: "
        print "3.if you want to exit:"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
        if ch==1:
            de=cl_Dept()
            de.update_dept()
        elif ch==2:
            from sub_options import suboptions
            su= suboptions()
            su.department_options()
        elif ch==3:
            exit()
        else:
            print "invalid choice, enter a correct choice:"
            return
    def find_dept(self):
        Deptno=raw_input("Enter Department Number:")
        f=open("department.txt","r")
        lines=f.readlines()
        for line in lines:
            words=line.split("\t")
            if words[0]==Deptno:
                print line
                print "The Department Data Found Successfully"
                break
        else:
            print "The Data Doesnot found on the Department number"
            f.close()
            print "*"*30
        print "Please go through below options:"
        print "1.If you want to find one more department: "
        print "2.If you want go to options of department: "
        print "3.if you want to exit:"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
        if ch==1:
            de=cl_Dept()
            de.find_dept()
        elif ch==2:
            from sub_options import suboptions
            su= suboptions()
            su.department_options()
        elif ch==3:
            exit()
        else:
            print "invalid choice, enter a correct choice:"
            return
    def list_dept(self):
        f=open("department.txt","r")
        lines=f.readlines()
        print "*"*50
        print "The Department Details in the Organization are:"
        print "*"*50
        for line in lines:
            print line
        f.close()
        print "The Details of each and every department in  the organization are displayed"
        print "*"*30
        print "Please go through below options:"
        print "1.If you want go to options of Department: "
        print "2.if you want to exit:"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
        if ch==1:
            from sub_options import suboptions
            su= suboptions()
            su.department_options()
        elif ch==2:
            exit()
        else:
            print "invalid choice, enter a correct choice:"
            return
    def delete_dept(self):
        Deptno=raw_input("Enter Department Number:")
        f=open("department.txt","r")
        lines=f.readlines()
        for i in range(len(lines)):
            words=lines[i].split("\t")
            if words[0]==Deptno:
                print lines[i]
                lines.pop(i)
                f=open("employee.txt","w")
                f.write("".join(lines))
                f.close()
                print "The Department Record was deleted"
                break
        else:
            print "There is no record on the Department Number"
            f.close()
            print "*"*30
        print "Please go through below options:"
        print "1.If you want to Delete one more Department: "
        print "2.If you want go to options of Department: "
        print "3.if you want to exit:"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
        if ch==1:
            de=cl_Dept()
            de.delete_dept()
        elif ch==2:
            from sub_options import suboptions
            su= suboptions()
            su.department_options()
        elif ch==3:
            exit()
        else:
            print "invalid choice, enter a correct choice:"
            return
de=cl_Dept()
#d.add_dept()
#d.update_dept()
#d.find_dept()
#d.list_dept()
#d.delete_dept()
