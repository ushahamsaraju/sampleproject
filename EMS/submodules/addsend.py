        Username=Email
        Password=id_generator()
        f=open("logindetails.txt","a")
        data="\n%s\t%s"%(Username,Password)
        f.write(data)
        f.close()
        print "Employee Added Successfully"
        to = Username
        gmail_user = 'bs.nivasreddy09@gmail.com'
        gmail_pwd = '9494295634'
        smtpserver = smtplib.SMTP('smtp.gmail.com',587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(gmail_user, gmail_pwd)
        header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:employee details added \n'
        detail='Welcome to Asterisk'+'\n'+'Hai '+Ename+',Your data added Successfully'+'\n'+ 'Username:'+Username+'\n'+'Password:'+Password
        smtpserver.sendmail(gmail_user, to,detail)
        print 'done!'
        smtpserver.close()
