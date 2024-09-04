import mysql.connector as mysql
mc=mysql.connect(host="localhost",user="root",passwd="12-07-2003",charset="utf8")
if mc.is_connected()==False:
    print("Database connectivity error")         #connecting with mysql
cursor=mc.cursor()
import stdiomask                               #importing stdiomask to let password in asterisks(pip install stdiomask)
import time                                     #importing time
from colored import fg,bg,attr          #importing colours (pip install colored) 
g=fg('green')
p=fg('light_pink_3')
o=fg('orange_3')
y=fg('light_yellow')                       
r=fg('orange_red_1')
w=fg('white')
c=fg('cyan')
m=fg('magenta')
cursor.execute('create database playup')
cursor.execute('use playup')
print('                                                                          PROJECT PLAYUP                                     ')
print('                                                                                      QUIZ                                                    ')

import BRplayupquiz

def achoice():
    import BRtable_correct
    BRtable_correct.abc()
    cursor.execute('select * from leaderboard')
    rec=cursor.fetchmany()
    print('Date','\t','Username','\t','Email_id','\t','Marks')
    for i in rec:
        for j in i:
            print(j,end='\t')
    print()
def bchoice(ans):
    if ans=='(b)'or ans=='b':
        print(c+'You have to login to make your own quiz')
        name=input(o+'Enter your name:')
        login_id=input(o+'Enter your Email address:')                    #login
        password=stdiomask.getpass(o+'Enter your Password:')
        re_enterpassword=stdiomask.getpass(o+'Enter your Password again to recheck:')
        T=True
        while T:                                                                        # checking password
            if password==re_enterpassword:
                print(g+'You have successfully logged in')                 
                T=False
            else:
                print(m+"Your password didn't match please re-enter your password")
                re_enterpassword=stdiomask.getpass('Enter your Password again to successfully login:')
        no=int(input(y+'How many quizes do you want to make? :'))
        for n in range(no):
            quizname=input('Enter your quiz name')                              #creating a table
            cursor.execute("create table %s (S_no int primary key, Questions varchar(100), A varchar(40),B varchar(40),C varchar(40), D varchar(40), Answers varchar(5), Ans varchar(3))" %quizname)
            Q_no=int(input('How many Questions do you want to put in this quiz? :'))
            cursor.execute('Set autocommit=0')
            for q in range(Q_no):
                S_no=q+1
                Questions=input(w+'Enter the question:')
                A=input('Enter part (a):')
                B=input('Enter part (b):')
                C=input('Enter part (c):')                                   
                D=input('Enter part (d):')
                Answers=input('Enter the answer option:')
                b='('
                s=')'
                s="%s""%s""%s" % (b,Answers,s)                                           #inserting values
                cursor.execute("insert into %s values({},'{}','{}','{}','{}','{}','{}','{}')".format(S_no,Questions,'%s ''%s' ,'%s ''%s','%s ''%s','%s ''%s',s,Answers) %(quizname,'(a)',A,'(b)',B,'(c)',C,'(d)',D))
                print(p+'(a) Do you save the content?\n(b) Do you want to make changes?')
                h=input('Enter your you choice:')
                if h=='(a)' or h=='a':
                    mc.commit()
                    print(g+'Your data is saved')
                elif h=='(b)' or h=='b':
                    cursor.execute('rollback')
                    Questions=input('Enter the question correctly:')
                    A=input('Enter part (a):')
                    B=input('Enter part (b):')
                    C=input('Enter part (c):')                                   
                    D=input('Enter part (d):')
                    Answers=input('Enter the answer option:')
                    b='('
                    s=')'
                    s="%s""%s""%s" % (b,Answers,s)                                           #inserting values
                    cursor.execute("insert into %s values({},'{}','{}','{}','{}','{}','{}','{}')".format(S_no,Questions,'%s ''%s' ,'%s ''%s','%s ''%s','%s ''%s',s,Answers) %(quizname,'(a)',A,'(b)',B,'(c)',C,'(d)',D))
                    mc.commit()
                    print(g+'Your changes is saved')
                else:
                    print('Wrong choice')
def cchoice(ans):                    
    if ans=='(c)' or ans=='c':
        print(y+'Here is the list of quizes:-')
        cursor.execute('show tables')
        r=cursor.fetchall()
        No=0
        for k in r:
            No=No+1
            if k[0]=='leaderboard':
                print(end='')
            else:
                print(No,'.',k[0])
        print('leaderboard is not a quiz this is your results')
        quiz=input(w+'which quiz do you want to play?\nGive the name of quiz:-')
        b=[]
        for k in r:
            b.append(k[0])
        for a in b:
            if a==quiz:
                cursor.execute("select * from %s"%quiz)
                records=cursor.fetchall()
                score=0
                print('3.......')
                time.sleep(3)                                                                    
                print('2.......')
                time.sleep(1)
                print('1.......')
                for i in records:
                    print(i[0],'.',i[1])
                    print(i[2])
                    print(i[3])
                    print(i[4])                              #displaying questions
                    print(i[5])
                    n=input('Enter your answer:')
                    try:
                        if n==i[6] or n==i[7]:
                            score+=1
                    except IndexError:
                        pass
                    continue
                time.sleep(3)
                Marks=round((score/i[0])*100,2)
                print(g+'Your scored',score,'out of',i[0],'\nYour precentage',round((score/i[0])*100,2),'%')              
                from BRleaderboard import date,p,login_id
                cursor.execute("insert into leaderboard values('{}','{}','{}',{})".format(date,p,login_id,Marks))
                mc.commit()
                cursor.execute('select * from leaderboard')
                rec=cursor.fetchmany()
                print('Date','\t','Username','\t','Email_id','\t','Marks’)
                for i in rec:
                    for j in i:
                        print(j,end='\t')
while True:
    print(o+'Select one option\n(a) Do you want to play quiz?\n(b) Do you want to create your own quiz?\n(c) Do you want choose a quiz of your liking?\n(d) Do you want to end the quiz?')
    ans=input('Enter your you choice:')
    if ans=='(a)' or ans=='a': 
        achoice()
    elif ans=='(b)'or ans=='b': 
        bchoice(ans) 
    elif ans=='(c)'or ans=='c': 
        cchoice(ans)
    elif ans=='(d)'or ans=='d':
        print(g+"Hope! You will play again next time :)")
        break 
    else: 
        print("Wrong choice")
input()
