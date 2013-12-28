from options import cl_log
from sub_options import *
class Mainfun():
    def main(self):
        print "*"*20
        print "Welcome To Asterisk Technologies"
        print "*"*20
        Username=raw_input("Enter a Username::")
        Password=raw_input("Enter a PassWord::")
        l=cl_log()
        l.login(Username,Password)
m=Mainfun()
m.main()
