def abc():
    import mysql.connector as mysql
    mc=mysql.connect(host="localhost",user="root",passwd="12-07-2003",charset="utf8")
    if mc.is_connected()==False:
        print("Database connectivity error")         #connecting with mysql
    cursor=mc.cursor()
    cursor.execute('use playup')
    from colored import fg,bg,attr          #importing colours
    g=fg('green')
    p=fg('light_pink_3')
    o=fg('orange_3')
    y=fg('light_yellow')                       
    r=fg('orange_red_1')
    w=fg('white')
    import time
    cursor.execute("select* from playupquiz1")
    records=cursor.fetchall()
    score=0
    print(p+'This is level-1 to test your knowledge\n')
    print(r+'3.......')
    time.sleep(3)                                                                         #working on option (a)
    print(y+'2.......')
    time.sleep(1)
    print(w+'1.......')
    for i in records:
        print(i[0],'.',i[1])
        print(i[2])
        print(i[3])
        print(i[4])                              #displaying questions
        print(i[5])
        n=input('Enter your answer:-')
        try:
            if n==i[6] or n==i[7]:
                score+=1
        except IndexError:
            pass
        continue
    time.sleep(3)
    print(g+'Your scored',score,'out of',i[0],'\nYour precentage',round((score/i[0])*100,2),'%')
    Marks1= round((score/i[0])*100,2)
    time.sleep(3)
    cursor.execute("select* from playupquiz2")
    rec=cursor.fetchall()
    score=0
    print(p+'This is level-2 to test your knowledge\n')
    print(r+'3.......')
    time.sleep(3)                                                                         #working on option (a)
    print(y+'2.......')
    time.sleep(1)
    print(w+'1.......')
    for i in rec:
        print(i[0],'.',i[1])
        print(i[2])
        print(i[3])
        print(i[4])                              #displaying questions
        print(i[5])
        n=input('Enter your answer:-')
        try:
            if n==i[6] or n==i[7]:
                score+=1
        except IndexError:
            pass
        continue
    time.sleep(3)
    print(g+'Your scored',score,'out of',i[0],'\nYour precentage',round((score/i[0])*100),'%')
    Marks2=round((score/i[0])*100,2)
    time.sleep(3)
    cursor.execute("select* from playupquiz3")
    rc=cursor.fetchall()
    score=0
    print(p+'This is level-3 to test your knowledge\n')
    print(r+'3.......')
    time.sleep(3)                                                                         #working on option (a)
    print(y+'2.......')
    time.sleep(1)
    print(w+'1.......')
    for i in rc:
        print(i[0],'.',i[1])
        print(i[2])
        print(i[3])
        print(i[4])                              #displaying questions
        print(i[5])
        n=input('Enter your answer:-')
        try:
            if n==i[6] or n==i[7]:
                score+=1
        except IndexError:
            pass
        continue
    time.sleep(3)
    print(g+'Your scored',score,'out of',i[0],'\nYour precentage',round((score/i[0])*100,2),'%')
    Marks3=round((score/i[0])*100,2)
    total=Marks1+Marks2+Marks3
    from BRleaderboard import date,p,login_id
    cursor.execute("insert into leaderboard values('{}','{}','{}',{})".format(date,p,login_id,total))
    mc.commit()
