class employee():
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
                                return
                else:
                        print "There is no record on the employee id"
                        f.close()
e=employee()
e.delete_employee()
