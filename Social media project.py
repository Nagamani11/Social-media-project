                               #SOCIAL MEDIA PROJECT-1

                 
'''
create table socialmedia(first_name varchar(50),last_name varchar(50), username varchar(50),
                         password varchar(50), confirm_password varchar(50), gender varchar(50),
                         email_id varchar(50), mobile bigint);
'''
'''
#Registration
import pymysql
import re
import string
connection =pymysql.connect(host='localhost',user='root',password='root',db='socialmediadb',charset='utf8')
c = connection.cursor()
c.execute('select * from socialmedia;')
data=c.fetchall()
uname = input('Enter username: ')
existing_user = []
existing_email =[]
for i in data:
    existing_user.append(i[2])
while True:
    if uname in existing_user:
        print('{} Alredy exist, use another username.format{uname}')
    else:
        fname = input('Enter your first_name: ')
        lname = input('Enter your last_name: ')
        while True:
            pwd1 = input('Enter your password: ')
            pwd2 = input('Enter  your confirm_password: ')
            if pwd1!=pwd2:
                print('password should be same')
                continue
            elif len([ i for i in pwd1 if i in string.ascii_lowercase]) == 0:
                print('It contain atleast one lowercase charecter')
                continue
            elif len([i for i in pwd1 if i in string.ascii_uppercase]) == 0:
                print('It contain atleast one uppercase charecter')
                continue
            elif len([i for i in pwd1 if i in string.digits]) == 0:
                print('It contains atleast one digit')
                continue
            elif len([i for i in pwd1 if i in string.punctuation]) == 0:
                print('It contains atleast one special charecter')
                continue
            elif len(pwd1)<8 or len(pwd1)>20:
                print('Password must be atleast 8 charecters atmost 20 charecters')
                continue
                
            else:
                while True:
                    gender = input('Enter your gender: ')
                    gender.lower()
                    g = ['male','female','others']
                    if gender not in g:
                        print('Enter valid gender')
                        continue
                    else:
                        while True:
                            email = input('Enter your email_id: ')
                            a=re.findall('[a-z]{1,}[0-9]{1,}@gmail.com',email)
                            if email in existing_email:
                                print('{} is already exist')
                                continue
                            if a == None:
                                print('Enter a valid email')
                                continue
                            else:
                                while True:
                                    mobile = input('Enter your mobile_number: ')
                                    m = re.fullmatch('[6-9]{1}[0-9]{1,}',mobile)
                                    if m == None:
                                        print('Mobile number must contains 10 digits')
                                        continue
                                    else:
                                        
                                        c.execute("insert into socialmedia values(%s,%s,%s,%s,%s,%s,%s,%s)",(fname,lname,uname,pwd1,pwd2,gender,email,mobile))
                                        connection.commit()
                                        print('Registration is successful!!!')
                                    break
                            break
                    break
            break
    break

#login
import pymysql
import re
import string
connection =pymysql.connect(host='localhost',user='root',password='root',db='socialmediadb',charset='utf8')
c = connection.cursor()
c.execute('select * from socialmedia;')
data=c.fetchall()
existing_user = []
for i in data:
    existing_user.append(i[2])

while True:
    username = input('Enter username: ')
    if username not in existing_user:
        print('Invalid username')
        continue
    else:
        while True:
            pwd = input('Enter your password: ')
            c.execute("select password from socialmedia where username = %s",(username))
            password = c.fetchall()
            if password[0][0] != pwd:
                print('Login Failed!!!')
                continue
            else:
                print('Login Successful!!!')
            break
    break

           
#Changing the password:
import pymysql
import re
import string
connection =pymysql.connect(host='localhost',user='root',password='root',db='socialmediadb',charset='utf8')
c = connection.cursor()
c.execute('select * from socialmedia;')
data=c.fetchall()
existing_user = []
for i in data:
    existing_user.append(i[2]) 
while True:
    username = input('Enter username: ')
    if username not in existing_user:
        print('Enter a valid username')
        continue
    else:
        while True:
            pwd = input('Enter Password: ')
            c.execute("select password from socialmedia where username = %s",(username))
            password = c.fetchall()
            if password[0][0] != pwd:
                print('Login Failed!!!')
    
            else:
                while True:
                    password = input('Enter New password: ')
                    confirm_password = input('Enter  your confirm_password: ')
                    if password!=confirm_password:
                        print('password should be same')
                        continue
                    elif len([ i for i in password if i in string.ascii_lowercase]) == 0:
                        print('It contain atleast one lowercase charecter')
                        continue
                    elif len([i for i in password if i in string.ascii_uppercase]) == 0:
                        print('It contain atleast one uppercase charecter')
                        continue
                    elif len([i for i in password if i in string.digits]) == 0:
                        print('It contains atleast one digit')
                        continue
                    elif len([i for i in password if i in string.punctuation]) == 0:
                        print('It contains atleast one special charecter')
                        continue
                    elif len(password)<8 or len(password)>20:
                         print('Password must be atleast 8 charecters atmost 20 charecters')
                         continue
                    else:
                        c.execute("update socialmedia set password = %s, confirm_password = %s where username = %s",(password,confirm_password,username))
                        connection.commit()
                        print('password changed successful!!!')
                    break
            break
    break
                  
#Update Details:
import pymysql
import re
import string
connection =pymysql.connect(host='localhost',user='root',password='root',db='socialmediadb',charset='utf8')
c = connection.cursor()
c.execute('select * from socialmedia;')
data=c.fetchall()
existing_user = []
existing_email = []
for i in data:
    existing_user.append(i[2]) 
while True:
    username = input('Enter username: ')
    if username not in existing_user:
        print('Enter a valid username')
        continue
    else:
        while True:
            pwd = input('Enter Password: ')
            c.execute("select password from socialmedia where username = %s",(username))
            password = c.fetchall()
            if password[0][0] != pwd:
                print('Login Failed!!!')
                continue
    
            else:
                fname = input('Enter your first_name: ')
                lname = input('Enter your last_name: ')
                while True:
                    email = input('Enter your email_id: ')
                    a=re.findall('[a-z]{1,}[0-9]{1,}@gmail.com',email)
                    if email in existing_email:
                        print('{} is already exist')
                        continue
                    if a == None:
                        print('Enter a valid email')
                        continue
                    else:
                        while True:
                            gender = input('Enter your gender: ')
                            gender.lower()
                            g = ['male','female','others']
                            if gender not in g:
                                print('Enter valid gender')
                                continue
                            else:
                                while True:
                                    mobile = input('Enter your mobile_number: ')
                                    m = re.fullmatch('[6-9]{1}[0-9]{1,}',mobile)
                                    if m == None:
                                        print('Mobile number must contains 10 digits')
                                        continue
                                    else:
                                        c.execute("update socialmedia set first_name = %s, last_name = %s, email_id = %s, gender = %s, mobile_number = %s where username = %s",(fname, lname, email, gender, mobile, username))
                                        connection.commit()
                                        print('Details Updated successfully!!!')
                                    break
                            break
                    break
            break
    break
'''                               
#Delete Account:
import pymysql
import re
import string
connection =pymysql.connect(host='localhost',user='root',password='root',db='socialmediadb',charset='utf8')
c = connection.cursor()
c.execute('select * from socialmedia;')
data=c.fetchall()
existing_user = []
for i in data:
    existing_user.append(i[2]) 
while True:
    username = input('Enter username: ')
    if username not in existing_user:
        print('Enter a valid username')
        continue
    else:
        while True:
            pwd = input('Enter Password: ')
            c.execute("select password from socialmedia where username = %s",(username))
            password = c.fetchall()
            if password[0][0] != pwd:
                print('Login Failed!!!')
                continue
            else:
                while True:
                    data = input('Do you want delete your account: ')
                    if data.lower() == 'yes':
                        print('Account Deleted Successfully!!!')
                        c.execute("delete from socialmedia where username = %s and password = %s",(username, password))
                        connection.commit()
                    elif data.lower() == 'no':
                        print('Account deletion is cancelled!!!')
                    else:
                        print('Choose either yes or no')
                        continue
                    break
            break
    break
                  
          
    

                
