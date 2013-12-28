class employee():
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
                f.close()
                f = open("employee.txt","w")        
                f.write("".join(lines))
                f.close()
                print " Employee details Updated Successfully"
                e.update_employee()
e=employee()
e.update_employee()
