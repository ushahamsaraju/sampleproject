import datetime
from validations import *
class cl_attendance():
    def add_attendance(self):
        Eid=v.validation_eno()
        month=raw_input("Enter Month no:")
        if  int(month) > datetime.datetime.today().month:
            print "enter valid month"
            add_attendance()
        year=raw_input("Enter year")
        leaves=raw_input("Enter leaves")
        org_wdays=raw_input("Enter org working days :")
        emp_wdays=str(int(org_wdays)-int(leaves))
        s=0
        #print emp_wdays
        f=open("reports.txt")
        ls=f.readlines()[1:]
        f.close()
        for l in ls:
            words=l.split("\t")
            if  eid == words[0] and month == words[4] :
                s=s+1
                #print ch
                break 
        if s == 0:
            f1=open("reports.txt","a")
            s="\n"+Eid+"\t"+org_wdays+"\t"+leaves+"\t"+emp_wdays+"\t"+month+"\t"+year
            try:
                f1.write(s)
                print "Record added"
                f1.close()
            except:
                print "Error occured"
                f1.close()
            else:
                print "Record already exists"
        print "Please go through below options:"
        print "1.If you want to add one more employee attendance: "
        print "2.If you want go to options of attendance: "
        print "3.if you want to exit:"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
        if ch==1:
            a=cl_attendance()
            a.add_attendance()
        elif ch==2:
            from sub_options import suboptions
            su= suboptions()
            su.attendance_options()
        elif ch==3:
            exit()
        else:
            print "invalid choice, enter a correct choice:"
            return

    def list_attendance(self):
         f = open("reports.txt","r")
         lines=f.readlines()
         print"the list of attendance:"+str(len(lines)-1)
         for line in lines:
             print line
             f.close()
         print "Please go through below options:"
        print "1.If you want go to options of attendance: "
        print "2.if you want to exit:"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
        if ch==1:
            from sub_options import suboptions
            su= suboptions()
            su.attendance_options()
        elif ch==2:
            exit()
        else:
            print "invalid choice, enter a correct choice:"
            return
    def search_attendance(self):
        eid=raw_input("Enter employee id:")
        f = open("reports.txt","r")
        lines=f.readlines()[1:]
        for line in lines:
            words=line.split("\t")
            if words[0]==eid:
                print lineimport.datetime
         print "Please go through below options:"
        print "1.If you want to find one more employee attendance: "
        print "2.If you want go to options of attendance: "
        print "3.if you want to exit:"
        try:
            ch=int(raw_input("Enter Your Choice:"))
        except Exception as e:
            print "The Error is :",e
            print "Please enter integers only"
        if ch==1:
            a=cl_attendance()
            a.search_attendance()
        elif ch==2:
            from sub_options import suboptions
            su= suboptions()
            su.attendance_options()
        elif ch==3:
            exit()
        else:
            print "invalid choice, enter a correct choice:"
            return
a=cl_attendance()
        
    
    
    
    
