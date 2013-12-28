from Employee import *
from Department import *
from project import *
from options import *
class suboptions():
    def employee_options(self):
        print "1. Add Employee"
        print "2. Update Employee"
        print "3. Find Employee"
        print "4. List Of Employee"
        print "5. Delete Employee"
        print "6. Goto Main Menu"
        print "7.Exit"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error :",e
            print "Please Enter Integers only"
        if ch==1:
            x=cl_Employee()
            x.add_employee()
            f=False
        elif ch==2:
            x=cl_Employee()
            x.update_employee()
            f=False
        elif ch==3:
            x=cl_Employee()
            x.find_employee()
            f=False
        elif ch==4:
            x=cl_Employee()
            x.list_employee()
            f=False
        elif ch==5:
            x=cl_Employee()
            x.delete_employee()
            f=False
        elif ch==6:
            print "Goto main options"
            from options import cl_log
            c=cl_log()
            c.admin_options()
            f=False
        elif ch==7:
            print "Thank you and ByeBye"
            f=False
            exit()
        else:
            print "Invalid Choice, please try again:"
    def department_options(self):
        print "1. Add Department"
        print "2. Update Department"
        print "3. Find Department"
        print "4. List Of Department"
        print "5. Delete Department"
        print "6. Goto Main Menu"
        print "7.Exit"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error :",e
            print "Please Enter Integers only"
        if ch==1:
            d=cl_Dept()
            d.add_dept()
            f=False
        elif ch==2:
            d=cl_Dept()
            d.update_dept()
            f=False
        elif ch==3:
            d=cl_Dept()
            d.find_dept()
            f=False
        elif ch==4:
            d=cl_Dept()
            d.list_dept()
            f=False
        elif ch==5:
            d=cl_Dept()
            d.delete_dept()
            f=False
        elif ch==6:
            print "Goto main menu"
            from options import cl_log
            f=False
            c=cl_log()
            c.admin_options()
        elif ch==7:
            exit()
        else:
            print "Please Enter a Valid Choice:"
    def project_options(self):
        print "1. Add Project"
        print "2. Update Project"
        print "3. Find Project"
        print "4. List Of Projects"
        print "5. Delete Project"
        print "6. Goto Main Menu"
        print "7.Exit"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error :",e
            print "Please Enter Integers only"
        if ch==1:
            p=cl_project()
            p.add_project()
            f=False
        elif ch==2:
            p=cl_project()
            p.update_project()
            f=False
        elif ch==3:
            p=cl_project()
            p.search_project()
            f=False
        elif ch==4:
            p=cl_project()
            p.list_project()
            f=False
        elif ch==5:
            p=cl_project()
            p.delete_project()
            f=False
        elif ch==6:
            print "Goto main menu"
            from options import cl_log
            f=False
            c=cl_log()
            c.admin_options()
        elif ch==7:
            exit()
        else:
            print "Please Enter a Valid Choice:"
    def attendance_options(self):
        print "1.Add_attendance"
        print "2. list_attendance"
        print "3.Search_attandance"
        print "4.Goto Main Menu"
        print "5.Exit"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error :",e
            print "Please Enter Integers only"
        if ch==1:
            at=cl_attendance()
            at.add_attendance()
            f=False
        elif ch==2:
            at=cl_attendance()
            at.list_attendance()
            f=False
        elif ch==3:
            at=cl_attendance()
            at.search_attendance()
            f=False
        elif ch==4:
            print "Goto main menu"
            from options import cl_log
            f=False
            c=cl_log()
            c.admin_options()
        elif ch==5:
            exit()
        else:
            print "Please Enter a Valid Choice:"        
    def Nonadmin_sub_options(self):
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
                    self.Nonadmin_sub_options()
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
                    self.Nonadmin_sub_options()
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
                    self.Nonadmin_sub_options()
                else:
                    print "Please Enter a Valid Choice:"
s=suboptions()
