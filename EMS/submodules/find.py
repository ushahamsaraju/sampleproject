class employee():
        def find_employee(self):
                Eid=raw_input("Enter Employee Number:")
                f=open("employee.txt","r")
                lines=f.readlines()
                for line in lines:
                    words=line.split("\t")
                    if words[0]==Eid:
                        print line
                        print "The Employee Data Found Successfully"
                        return
                else:
                        print "The Data Doesnot found on the Employee number"                    
                        f.close()               
e=employee()
e.find_employee()
