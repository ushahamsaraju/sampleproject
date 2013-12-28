class employee():
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
e=employee()
e.list_employee()
