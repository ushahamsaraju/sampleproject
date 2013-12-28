import re
from validations import *
import smtplib
class cl_project():
    def add_project(self):
        Pid=v.validation_pid()
        Pname=raw_input("Enter Project  Name:")
        Teamsize=v.validation_psize()
        Pdomain=raw_input("Enter the Domain of Project:")
        Pclient=raw_input("Enter Project Client name:")
        Pmanager=raw_input("Enter the name of Project Manager:")
        f=open("project.txt","a")
        data="%s\t%s\t%s\t%s\t%s\t%s\n"%(Pid,Pname,Teamsize,Pdomain,Pclient,Pmanager)
        f.write(data)        
        f.close()
        print "You have Added successfully"
        print "*"*30
        print "1.If you want to add one more project: "
        print "2.If you want go to options of project: "
        print "3.if you want to exit:"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
        if ch==1:
            p=cl_project()
            p.add_project()
        elif ch==2:
            from sub_options import suboptions
            su= suboptions()
            su.project_options()
        elif ch==3:
            exit()
        else:
            print "invalid choice, enter a correct choice:"
            return
    def update_project(self):
        Pid=raw_input("Enter project id:")
        new=raw_input("Enter project new size:")
        f = open("project.txt","r")
        lines=f.readlines()
        #t = lines[:]
        #lines = lines[1:]
        for i in range(len(lines)):
            words=lines[i].split("\t")
            if words[0] == Pid:
                lines[i] = lines[i].replace(words[2],new)
                print lines[i]
                break
        else:
            print "Record Not Found"
            return
        f.close()
        with open("project.txt","w") as f:
            f.write("".join(lines))
            f.close()
            print " Employee details Updated Successfully"
        print "1.If you want to find one more project: "
        print "2.If you want go to options of project: "
        print "3.if you want to exit:"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
        if ch==1:
            p=cl_project()
            p.update_project()
        elif ch==2:
            from sub_options import suboptions
            su= suboptions()
            su.project_options()
        elif ch==3:
            exit()
        else:
            print "invalid choice, enter a correct choice:"
            return
    def search_project(self):
        Pname=raw_input("Enter project name:")
        f = open("project.txt","r")
        lines=f.readlines()
        for line in lines:
            words=line.split("\t")
            if words[1]==Pname:
                print line
                print Pname,":project is founded" 
                break
        else:
            print "project not founded"
            f.close()
        print "1.If you want to find one more project: "
        print "2.If you want go to options of project: "
        print "3.if you want to exit:"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
        if ch==1:
            p=cl_project()
            p.search_project()
        elif ch==2:
            from sub_options import suboptions
            su= suboptions()
            su.project_options()
        elif ch==3:
            exit()
        else:
            print "invalid choice, enter a correct choice:"
            return
    def list_project(self):
        f = open("project.txt","r")
        lines=f.readlines()
        print"the list of projects are:"+str(len(lines)-1)
        for line in lines:
            print line
            f.close()
        print "1.If you want go to options of project: "
        print "2.if you want to exit:"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
        if ch==1:
            from sub_options import suboptions
            su= suboptions()
            su.project_options()
        elif ch==2:
            exit()
        else:
            print "invalid choice, enter a correct choice:"
            return
    def delete_project(self):
        Pname = raw_input("enter which project name to deleta:")
        with open("project.txt", "r") as f:
            lines = f.readlines()
            t = lines
            for i in range(len(lines)):
                words=lines[i].split("\t")
                if str(words[1]) == Pname:
                    print lines[i]
                    t.pop(i)
                    f = open("project.txt","w")
                    #f.write("Pidname\tpid\tpmanager\tduration\n")
                    f.write("".join(t))
                    f.close()
                    print " project details deleted Successfully"
                    break
            else:
                print "project not found: "
                print "*"*30
        print "1.If you want to delete one more project: "
        print "2.If you want go to options of project: "
        print "3.if you want to exit:"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
        if ch==1:
            p=cl_project()
            p.delete_project()
        elif ch==2:
            from sub_options import suboptions
            su= suboptions()
            su.project_options()
        elif ch==3:
            exit()
        else:
            print "invalid choice, enter a correct choice:"
            return
    
pr=cl_project()
#p.add_project()
#p.update_project()
#p.search_project()
#p.list_project()
#p.delete_project()
