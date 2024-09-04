import mysql.connector as mysql
mc=mysql.connect(host="localhost",user="root",passwd="12-07-2003",charset="utf8")
if mc.is_connected()==False:
    print("Database connectivity error")         #connecting with mysql
cursor=mc.cursor()
import stdiomask
import datetime
cursor.execute('use playup')
cursor.execute('create table leaderboard (Date date,Username varchar(30),Email_add varchar(50),Marks decimal(10,2))')
print('(a) Do you want to sign in quiz?\n(b) Do you want to login?')
choice=input('Enter your choice')
if choice=='a':
    p=input('Enter Your Username')
    date=datetime.date.today()
    login_id=input('Enter your Email address:')
    password=stdiomask.getpass('Enter your Password:')
    re_enterpassword=stdiomask.getpass('Enter your Password again to recheck:')
    T=True
    while T:                                                                        # checking password
        if password==re_enterpassword:
            print('You have successfully logged in')                 
            T=False
        else:
            print("Your password didn't match please re-enter your password")
            re_enterpassword=stdiomask.getpass('Enter your Password again to successfully login:')
import BRplayupquiz
import BRtable_correct
