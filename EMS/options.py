#from Employee import *
#from Department import *
#from validations import *
from sub_options import *
class cl_log():
    def login(self,Username,Password):
        f=open("logindetails.txt","r")
        lines=f.readlines()[1:]
        for line in lines:
            words=line.split("\t")
            if words[0].strip() == Username and words[1].strip() == Password:
                if words[2].strip() == "admin":
                    print "-"*30
                    print "WELCOME TO ADMINISTRATOR"
                    print "-"*30
                    self.admin_options()
                    return
                else:
                    print "-"*30
                    print "WELCOME TO NON ADMINISTRATOR"
                    print "-"*30
                    self.nonadmin_options()
                    return
        else:
            print "Invalid User Name and Password"
            from main import Mainfun
            o =Mainfun()
            o.main()
    def admin_options(self):
        print "The Administrator Options are::"
        print "1. Employee\n2. Department\n3. Project\n4. Attendance\n5. Leaves\n 6. Appraisal\n 7.Exit "
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
          # self.admin_options()
        if ch==1:
            f=True
            while f:
                print "*"*30
                print "Welcome To Employee Data"
                print "*"*30
                eop=suboptions()
                eop.employee_options()
        elif ch==2:
            f=True
            while f:
                print "*"*30
                print "Welcome To Department Data"
                print "*"*30
                eop=suboptions()
                eop.department_options()
        elif ch==3:
            f=True
            while f:
                print "*"*30
                print "Welcome To Project Data"
                print "*"*30
                eop=suboptions()
                eop.project_options()
        elif ch==4:
            f=True
            while f:
                print "*"*30
                print "Welcome To Attendance Reports"
                print "*"*30
                eop=suboptions()
                eop.attendance_options()       
    def nonadmin_options(self):
        print "The Non Administrator Options are::"
        print "1. Employee\n2. Department\n3. Attendance\n4. Leaves\n 5. Appraisal\n6. Project\n 7.Exit "
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
           #self.nonadmin_options()
        if ch==1:
            f=True
            while f:
                print "*"*30
                print "Welcome To Employee Data"
                print "*"*30
                print "1. Update Employee"
                print "2. Find Employee"
                print "3. List Of Employee"
                print "4. Goto Main Menu"
                try:
                    ch=int(raw_input("Enter Your Choice:"))
                except Exception as e:
                    print "The Error :",e
                    print "Please Enter Integers only"
                if ch==1:
                    e=cl_Employee()
                    e.update_employee()
                    f=False
                elif ch==2:
                    e=cl_Employee()
                    e.find_employee()
                    f=False
                elif ch==3:
                    e=cl_Employee()
                    e.list_employee()
                    f=False
                elif ch==4:
                    print "Goto Main menu"
                    f=False
                    self.nonadmin_options()
                else:
                    print "Please Enter a Valid Choice:"
        elif ch==2:
            f=True
            while f:
                print "*"*30
                print "Welcome To Department Module"
                print "*"*30
                print "1. Find Department"
                print "2. List Of Department"
                print "3. Goto Main Menu"
                try:
                    ch=int(raw_input("Enter Your Choice:"))
                except Exception as e:
                    print "The Error :",e
                    print "Please Enter Integers only"
                if ch==1:
                    d=cl_Dept()
                    d.find_dept()
                    f=False
                elif ch==2:
                    d=cl_Dept()
                    d.list_dept()
                    f=False
                elif ch==3:
                    print "GOto main menu"
                    f=False
                    self.nonadmin_options()
                else:
                    print "Please Enter a Valid Choice:"
        elif ch==3:
            f=True
            while f:
                print "*"*30
                print "Welcome To Project Module"
                print "*"*30
                print "1. Find Project"
                print "2. List Of Project"
                print "3. Goto Main Menu"
                try:
                    ch=int(raw_input("Enter Your Choice:"))
                except Exception as e:
                    print "The Error :",e
                    print "Please Enter Integers only"
                if ch==1:
                    p=cl_project()
                    p.search_project()
                    f=False
                elif ch==2:
                    p=cl_project()
                    p.list_project()
                    f=False
                elif ch==3:
                    print "GOto main menu"
                    f=False
                    self.nonadmin_options()
                else:
                    print "Please Enter a Valid Choice:"
