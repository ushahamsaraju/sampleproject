import re
class validate():
    def validation_Empno(self):
        data = []
        with open("employee.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                data.append(line.split("\t")[0])
        while True:
            try:
                Eid=int(raw_input("Enter Employee Number:"))
            except Exception:
                    print "Please Try Again , Enter only numbers:"
                    print "Enter Integers only"
                    continue
            if str(Eid) in data:
                print "Employee ID already exists and please Enter New number:"
                #Eid=raw_input("Enter Employee Number:")
            else:
                break
        return Eid
    def validation_eno(self):
        #Validation of emp no in attendance
        l=[]
        with open("employee.txt","r") as f:
            lines=f.readlines()[1:]
            for line in lines:
                l.append(line.split("\t")[0])
        while True:
            try:
                Empno=int(raw_input("Enter employee number:"))
            except Exception:
                print "Please Try again with numbers only:"
                continue
            if str(Empno) in l:
                return Empno
            else:
                print "enter wrong employee id plaase try again with below ids: ",l
                continue      
    def validation_deptno(self):
        #for Adding Deptno to Employeee Table
        data = []
        with open("department.txt", "r") as f:
            lines = f.readlines()[1:]
            for line in lines:
                data.append(line.split("\t")[0])
        while True:
            try:
                Deptno=int(raw_input("Enter Department Number:"))
            except Exception:
                print "Please Try Again , Enter only numbers:"
                continue
            if str(Deptno)  in data:
                return Deptno
            else:
                print "Enter wrong option please try again with the following",data
                continue
    def validation_dno(self):
        # for Adding Deptno to Dept Table
        data=[]
        with open("department.txt","r") as f:
            lines=f.readlines()[1:]
            for line in lines:
                data.append(line.split("\t")[0])
        while True:
            try:
                Deptno=int(raw_input("Enter Department Number:"))
            except Exception:
                print "Enter Intergers only, please Try again:"
                continue
            if len(str(Deptno))==2:
                if str(Deptno) not in data:
                    return Deptno
                else:
                    print "Entered Dept no is Already exists, please try again:"
                    continue
            else:
                print "Enter two digits number only like :",data
                continue
                    
    def validation_pid(self):
        data = []
        with open("project.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                data.append(line.split("\t")[0])
        while True:
            try:
                Pid=int(raw_input("Enter Project Id:"))
            except Exception:
                print "Please Try Again , Enter only numbers:"
                print "Enter Integers only"
                continue
            if str(Pid) in data:
                print "Project ID already exists and please Enter New number:"
                #Eid=raw_input("Enter Employee Number:")
            else:
                break
        return Pid      
    def validation_Salary(self):
        flag=True
        while flag:
            try:
                Salary = int(raw_input("Enter Employee Salary:"))
            except Exception:
                print "Salary should be integers"
            else:
                if int(Salary)>0:
                    flag=False
                    return Salary
                else:
                    print "Salary Should be Positive, please enter correctely"
    def validation_Email(self):
        flag = True
        while flag:
            Email = raw_input("Please Enter Email :")
            if re.search('\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+',Email):
                flag = False
                return Email
            else:
                print "Invalid Email, Please try again."
    def validation_Phno(self):
        flag = True
        while flag:
            try:
                Phno = int(raw_input("Please Enter 10 digit Mobile Number :"))
            except Exception:
                print "Enter only numbers, Please try again:"
                continue
            if len(str(Phno)) == 10:
                flag = False
                return Phno
            else:
                print "Invalid Phone Number, Please try again."
    def validation_psize(self):
        flag=True
        while flag:
            try:
                Teamsize=int(raw_input("Enter a Project team size"))
            except Exception:
                print "Enter only numericals, try again:"
                continue
            if Teamsize >=12 and Teamsize <=100:
                flag=False
                return Teamsize
            else:
                print "Invalid Size, please enter the size number between 12 and 100"                
v=validate()
#v.validation_deptno()
#v.validation_dno()
