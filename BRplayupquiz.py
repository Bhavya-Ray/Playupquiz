import mysql.connector as mysql
mc=mysql.connect(host="localhost",user="root",passwd="12-07-2003",charset="utf8")
if mc.is_connected()==False:
    print("Database connectivity error")         #connecting with mysql
cursor=mc.cursor()

cursor.execute('use playup')
#Table1
cursor.execute('create table playupquiz1(S_no int primary key, Questions varchar(80), A varchar(30), B varchar(30), C varchar(30), D varchar(30), Answers varchar(5), Ans varchar(5))')
cursor.execute('insert into playupquiz1 values(1,"Who is the father of our nation?", "(a) Rajendra Parsad","(b) Mahatma Gandhi","(c) B.R.Ambedkar","(d) Jawaharlal Nehru", "(b)", "b")')
cursor.execute('insert into playupquiz1 values(2,"Who was the first president of India?", "(a) Rajendra Parsad","(b) Mahatma Gandhi","(c) Sardar vallabhbhai Patel","(d) Jawaharlal Nehru", "(a)", "a")')
cursor.execute('insert into playupquiz1 values(3,"Who wrote Romeo and Juliet?", "(a) Ruskin Bond","(b) A.R.Barton","(c) William Douglas","(d) William Shakespeare", "(d)", "d")')
cursor.execute('insert into playupquiz1 values(4,"Who wrote the National song - Vande Matram?", "(a) Bankim Chandra Chatterjee","(b) Amiya Tagore","(c) Rabindra Nath Tagore","(d) Sharbani Sen", "(a)", "a")')
cursor.execute('insert into playupquiz1 values(5,"Fathometer is used to measure", "(a) Earthquaks","(b) Rainfall","(c) Ocean Depth","(d) Sound Intensity", "(c)", "c")')
cursor.execute('insert into playupquiz1 values(6,"Epsom(England) is the place associated with", "(a) Snooker","(b) Shooting","(c) Polo","(d) Horse racing", "(d)", "d")')
cursor.execute('insert into playupquiz1 values(7,"When is the International Yoga Day celebrated?", "(a) May 31","(b) March 21","(c) April 22","(d) June 21", "(d)", "d")')
cursor.execute('insert into playupquiz1 values(8,"The World largest desert is ", "(a) Thar","(b) Kalahari","(c) Sahara","(d) Sonoran", "(c)", "c")')
cursor.execute('insert into playupquiz1 values(9,"January 15 is celebrated as", "(a) Army Day","(b) Ugadhi","(c) Teachers Day","(d) Republic Day", "(a)", "a")')
cursor.execute('insert into playupquiz1 values(10,"Which is known as:-Garden City of India?", "(a) Thiruvananthapuram","(b) Imphal","(c) Shimla","(d) Bangalore", "(d)", "d")')
#Table2
cursor.execute('create table playupquiz2(S_no int primary key, Questions varchar(100), A varchar(50), B varchar(50), C varchar(50), D varchar(50), Answers varchar(5), Ans varchar(5))')
cursor.execute('insert into playupquiz2 values(1,"Creatures that can live in extreme environments are", "(a) Hooligans","(b) Extremophiles","(c) Extremely rare","(d) Extremists", "(b)", "b")')
cursor.execute('insert into playupquiz2 values(2,"Vitamin E is important for", "(a) Protecting cells","(b) Vital tissues protection","(c) Both a and b","(d) Development of bones", "(c)", "c")')
cursor.execute('insert into playupquiz2 values(3,"A disease Kwashiorkor is caused by the deficiency of", "(a) Vitamins","(b) Proteins","(c) Carbohydrates","(d) Fats", "(b)", "b")')
cursor.execute('insert into playupquiz2 values(4,"The Battle of Waterloo was fought in the year", "(a) 1876","(b) 1715","(c) 1815","(d) 1915", "(c)", "c")')
cursor.execute('insert into playupquiz2 values(5,"World Cup is associated with?", "(a) Tenis","(b) Golf","(c) Football","(d) None of these", "(c)", "c")')
cursor.execute('insert into playupquiz2 values(6,"How many Country are there in Asia?", "(a) Thirty three countries","(b) Forty nine countries","(c) Forty seven countries","(d) None of These", "(b)", "b")')
cursor.execute('insert into playupquiz2 values(7," The 2019 C40 World Mayors Summit to be held in which city?", "(a) Copenhagen","(b) Washington","(c) New Delhi","(d) Berlin", "(a)", "a")')
cursor.execute('insert into playupquiz2 values(8,"Which of the following is planning to invest in technology start-ups in India?", "(a) Google Alphabet","(b) Intel Corp ","(c) Apple","(d) Facebook", "(d)", "d")')
cursor.execute('insert into playupquiz2 values(9,"Which Insurance Policy is launched to cover the hospitalisation expenses of the COVID-19 patients?", "(a) LIC Jeevan Saral","(b) Jeevan Saral","(c) Jeevan Anand","(d) Arogya Sanjeevani Insurance Policy", "(d)", "d")')
cursor.execute('insert into playupquiz2 values(10,"Green coloured vegetables are rich source of", "(a) Vitamin B","(b) Vitamin C","(c) Vitamin A","(d) None of These", "(c)", "c")')
#Table3
cursor.execute('create table playupquiz3(S_no int primary key, Questions varchar(100), A varchar(50), B varchar(50), C varchar(50), D varchar(50), Answers varchar(5), Ans varchar(5))')
cursor.execute('insert into playupquiz3 values(1,"Durand Cup is associated with?", "(a) Polo","(b) Cricket","(c) Golf","(d) Football", "(d)", "d")')
cursor.execute('insert into playupquiz3 values(2,"Tribal Dance Festival will be held in which of the following cities?", "(a) Indore","(b) Raipur","(c) Ranchi","(d) Kohima", "(b)", "b")')
cursor.execute('insert into playupquiz3 values(3,"Which IIT institute will start ‘Vastu Shastra’ classes for architecture students?", "(a) IIT Kharagpur","(b) IIT Bombay","(c) IIT Madras","(d) IIT Indore", "(a)", "a")')
cursor.execute('insert into playupquiz3 values(4,"Who was the Roman Emperor when Jesus was born?", "(a) Julius Caesar","(b) Caligula","(c) Augustus","(d) None of these", "(c)", "c")')
cursor.execute('insert into playupquiz3 values(5,"DDT stands for", "(a) Dichloro Diphenyl Trichloroethane","(b) Dichloro Triphenyl Dichloroethane","(c) Dichloro Triammomium Methane","(d) Difluoro Diphenyl Tribromobutane", "(a)", "a")')
cursor.execute('insert into playupquiz3 values(6,"Which of these poet’s was popularly known As Vikatakavi?", "(a) Chand Bardai","(b) Kalidasa","(c) Banabhatta","(d) Tenali Ram", "(d)", "d")')
cursor.execute('insert into playupquiz3 values(7,"Who was the first governor of RBI who later became the Finance minister of India?", "(a) Manmohan Singh","(b) I G Patel","(c) Bengal Rama Rau","(d) C.D. Deshmukh ", "(d)", "d")')
cursor.execute('insert into playupquiz3 values(8,"Who is called the father of computer? ", "(a) Herman Holerith","(b) Charles Babbage","(c) Wales Pascle","(d) Wen Newmaan", "(b)", "b")')
cursor.execute('insert into playupquiz3 values(9,"Which of the following Indian Mobile app clinched the bronze medal at the Technovation Challenge?", "(a) Maitri","(b) VithU","(c) Nirbhaya","(d) YatraMiTR", "(a)", "a")')
cursor.execute('insert into playupquiz3 values(10,"Which was first virus detected on ARPANET, the forerunner of the internet in the early 1970s?", "(a) Exe Flie","(b) Creeper Virus","(c) Peeper Virus","(d) Trozen horse", "(b)", "b")')

mc.commit()

mc.close()
