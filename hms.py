import mysql.connector as sql
mydb=sql.connect(host='localhost',user='root',password='jnv@123')
mycursor=mydb.cursor()

print('*'*60)
print(' '*15,'City Hospital')
print('*'*60)
#mycursor.execute("drop database hms")
mycursor.execute("create database hms")

mycursor.execute("use hms")

mydb.commit()

mycursor.execute("create table patient(pat_id int,room_no int, pat_name varchar(50),age int,gender char(1),blood_group varchar(3),problem varchar(70),ph bigint, E_date date,Discharge_date date)")
mydb.commit()
mycursor.execute("create table doctor(doc_id int,doc_name varchar(50), age int,department varchar(50),ph bigint)")
mydb.commit()
mycursor.execute("create table bill(pat_id int,pat_name varchar(50),Bed_charges int,Med_charges int,Doc_charges int,total int)")
mydb.commit()
mycursor.execute("create table worker(worker_id int,worker_name varchar(50),Designation varchar(50),age int, Date_of_join date, ph bigint)")
mydb.commit()
mycursor.execute("create table appointment(doc_id int,doc_name varchar(50),pat_name varchar(50),department varchar(50),date int)")
mycursor.execute("create table lab(lab_id int,pat_id int,pat_name varchar(50),age int,test_type varchar(50),Date date,ph bigint)")
mydb.commit() 

print('You are a ')
print('1. Admin')
print('2. Receptionist')
print('3. Patient')
print('4. Doctor')
print('5. Accountant')
print('6. Lab Attender')

lv=int(input("enter choice"))
if lv==1:
    print("1.Login")
    print("2.Exit")
    ch=int(input("enter choice"))
    if ch==1:
        u1=input("Enter Username")
        pwd1=input("Enter Password")
        if u1=='city_hospital' and pwd1=='tiger123':
            print('Login successful')
            print()
        while u1=='city_hospital' and pwd1=='tiger123':
             print("1. Patient")
             print("2. Doctor")
             print('3. Worker')
             print("4. Lab")
             print("5. Bill")
             print("6. Exit")
             choice=int(input("enter choice"))
             if choice==1:
                 print("*"*50)
                 while choice==1:
                     print('1.Patient Registration')
                     print('2. Details of patient')
                     print("3. Patient discharge registration")
                     print('4. Remove patient')
                     print('5.exit')
                     c1=int(input("enter ch"))
                     if c1==1:
                         print("*"*50)
                         pat_id=int(input("enter id"))
                         room_no=int(input("room no"))
                         pat_name=input("patient name")
                         age=int(input("age"))
                         gender=input("gender")
                         bg=input("Enter blood group")
                         problem=input("Enter the disease")
                         ph=int(input('Enter ph'))
                         E_date=input("Enter entry date")
                         mycursor.execute("insert into patient values({},{},'{}',{},'{}','{}','{}',{},'{}')".format(pat_id,room_no,pat_name,age,gender,bg,problem,ph,E_date))
                         mydb.commit()
                     elif c1==2:
                        print('*'*50)
                        h= input("Enter patient name or type 'all' for all the details ")
                        if h=='all':
                            print("*"*50)
                            sql_w='select * from patient'
                            mycursor.execute(sql_w)
                            s=mycursor.fetchall()
                            for i in s:
                                print(i)
                                print("*"*50)
                        else:
                            sql_w='select * from patient where pat_name=("{}")'
                            mycursor.execute(sql_w.format(h))
                            for i in u:
                                print(i)
                                print('*'*50)
                               
                     elif c1==4:
                        print('*'*50)
                        h= int(input('Enter patient id'))
                        sql_w='delete from patient where pat_id=({})'
                        mycursor.execute(sql_w.format(h))
                        print('Deletion done')
                     elif c1==3:
                        dis_date=input("enter dicharge date")
                        p_id=int(input("enter patient id"))
                        sql = "UPDATE table SET Discharge_date = ? WHERE pat_id = ?"
                        mycursor.execute(sql,(p_id, dis_date))
                        print('done')
                     elif c1==5:
                        break
             elif choice==2:
                print("*"*50)
                while choice==2:
                    print('1. Add doctor')
                    print('2. Details of doctor')
                    print('3. Remove doctor')
                    print('4. Exit')
                    c1=int(input("enter ch"))
                    if c1==1:
                          print("*"*50)
                          doc_id=int(input("enter doctor id "))
                          doc_name=input("doctor name")
                          age=int(input("age"))
                          department=input("enter depart")
                          ph=int(input('enter ph'))
                          sq ='insert into doctor values({},"{}",{},"{}",{})'
                          mycursor.execute(sq.format(doc_id,doc_name,age,depart,ph))
                          mydb.commit()
                    elif c1==2:
                        print('*'*50)
                        h= input("Enter doctor name or type 'all' for all the details ")
                        if h=='all':
                            print("*"*50)
                            sql_w='select * from doctor'
                            mycursor.execute(sql_w)
                            s=mycursor.fetchall()
                            for i in s:
                                print(i)
                                print("*"*50)
                        else:
                            h=int(h)
                            sql_w='select * from doctor where doc_id=({})'
                            mycursor.execute(sql_w.format(h))
                    elif c1==3:
                        print('*'*50)
                        h= int(input('Enter Doctor id'))
                        sql_w='delete from doctor where doc_id=({})'
                        cl.execute(sql_w.format(h))
                        print('Deletion done')
                    else:
                        break
             elif choice==3:
                print("*"*50)
                while choice==3:
                    print('1. Add worker')
                    print('2. Details of worker')
                    print('3. Remove worker')
                    print('4. Exit')
                    c1=int(input("enter ch"))
                    if c1==1:
                          print("*"*50)
                          doc_id=int(input("enter worker id "))
                          doc_name=input("worker name")
                          age=int(input("age"))
                          department=input("enter department")
                          ph=int(input('enter ph'))
                          sq ='insert into worker values({},"{}",{},"{}",{})'
                          mycursor.execute(sq.format(doc_id,doc_name,age,depart,ph))
                          mydb.commit()
                    elif c1==2:      
                        print('*'*50)
                        h= input("Enter worker name or type 'all' for all the details ")
                        if h=='all':
                            print("*"*50)
                            sql_w='select * from worker'
                            mycursor.execute(sql_w)
                            s=mycursor.fetchall()
                            for i in s:
                                print(i)
                                print("*"*50)
                        else:
                            sql_w='select * from worker where worker_id=({})'
                            mycursor.execute(sql_w.format(h))
                    elif c1==3:
                        print('*'*50)
                        h= int(input('Enter worker id'))
                        sql_w='delete from worker where worker_id=({})'
                        cl.execute(sql_w.format(h))
                        print('Deletion done')
                    else:
                        break
            
             elif choice==4:
               print("*"*50)
               
               while choice==1:
                   print('1.Add record')
                   print('2.display record')
                   print('3. remove record')
                   print('4.exit')
                   c1=int(input("enter ch"))
                   if c1==1:
                       print("*"*50)
                       lab_id=int(input("enter lab id "))
                       department=input("Department  name")
                       pat_id=int(input("Patient id"))
                       pat_name=input("Patient name")
                       age=int(input("enter age "))
                       test_type=input('enter test type')
                       Date=input("enter date")
                       ph=int(input("enter phone no"))
                       sq='insert into lab values({},"{}",{},{},"{}","{}","{}",{})'
                       mycursor.execute(sq.format(lab_id,department,pat_id,pat_name,age,test_type,Date,ph))
                       mydb.commit()
                   elif c1==2:
                       print("*"*50)
                       h= input("Enter patient name or type 'all' for all the details ")
                       if h=='all':
                           print("*"*50)
                           sql_w='select * from lab'
                           mycursor.execute(sql_w)
                           s=mycursor.fetchall()
                           for i in s:
                               print(i)
                               print("*"*50)
                       else:
                           sql_w='select * from lab where pat_name=("{}")'
                           cl.execute(sql_w.format(h))
                   elif ch==3:
                       print("*"*50)
                       h= int(input('Enter patient id'))
                       sql_w='delete from lab where pat_name=("{}")'
                       mycursor.execute(sql_w.format(h))
                       print('Deletion done')
                       
                   elif ch==4:
                       break
             elif choice==5:
                     print("*"*50)
                     print('1.To view the bills')
                     print('2. Exit')
                     c1=int(input("enter ch"))
                     if c1==1:
                         sql_w='select * from bill'
                         mycursor.execute(sql_w)
                         s=mycursor.fetchall()
                         for i in s:
                             print(i)
                             print("*"*50)
                     elif c1==2:
                        break
 
             elif choice==6:
                break
if lv==2:
    while True:
        print("1. Patient")
        print("2. Exit")
        choice=int(input("Enter choice"))
        if choice==1:
            print("*"*50)
            while choice==1:
                print('1.Patient Registration')
                print('2. Details of patient')
                print("3. Patient discharge registration")
                print('4. Remove patient')
                print('5.exit')
                c1=int(input("enter ch"))
                if c1==1:
                    print("*"*50)
                    pat_id=int(input("enter id"))
                    room_no=int(input("room no"))
                    pat_name=input("patient name")
                    age=int(input("age"))
                    gender=input("gender")
                    bg=input("Enter blood group")
                    problem=input("Enter the disease")
                    ph=int(input('Enter Phone Number'))
                    E_date=input("Enter entry date")
                    mycursor.execute("insert into patient(pat_id,room_no,pat_name,age,gender,blood_group,problem,ph,E_date) values({},{},'{}',{},'{}','{}','{}',{},'{}')".format(pat_id,room_no, pat_name,age,gender,bg,problem,ph,E_date))
                    mydb.commit()
                    print('Registration Successful')
                elif c1==2:
                    print('*'*50)   
                    h=input("Enter patient ID or type 'all ' for all the details ")
                    if h=='all':
                        print("*"*50)
                        sql_w='select * from patient'
                        mycursor.execute(sql_w)
                        s=mycursor.fetchall()
                        for i in s:
                            print(i)
                            print("*"*50)
                    else:
                        sql_w='select * from patient where pat_id=("{}")'
                        mycursor.execute(sql_w.format(int(h)))
                        s=mycursor.fetchall()
                        for i in s:
                            print(i)
                            print('*'*50)

                elif c1==4:
                    print('*'*50)
                    print(' '*50)
                    h= int(input('Enter patient id'))
                    sql_w='delete from patient where pat_id=({})'
                    mycursor.execute(sql_w.format(h))
                    print('Deletion done')
                elif c1==3:
                    p_id=int(input("enter patient id"))
                    dis_date=input("enter dicharge date")
                    sq="UPDATE patient SET Discharge_date=%s WHERE pat_id=%s"
                    mycursor.execute(sq,(dis_date,p_id))
                    print('done')
                elif c1==5:
                    break
                    
        elif choice==2:
            break
           
elif lv==3:
     while True:
        print("1.Add Appointment")
        print("2.Remove Appointment")
        choice=int(input("Enter choice"))
        if choice==1:
            print("*"*50)
            pat_name=input('Enter your name')
            print("For Appointment")
            input('Press Enter')
            co='select distinct department from doctor;'
            mycursor.execute(co)
            s=mycursor.fetchall()
            for i in s:
                print(i)
                print("*"*50)
            dept=input('Enter the specialisation')
            com='select doc_id,doc_name,ph from doctor where department=("{}")'
            mycursor.execute(com.format(dept))
            s=mycursor.fetchall()
            for i in s:
               print(i)
               print("*"*50)
            name=input('Enter the name of the doctor')
            id1=input('Enter the id of the doctor')
            date=input('Enter the date of appointment(yyyy-mm-dd)')
            mycursor.execute('insert into appointment values({},"{}","{}","{}",{})'.format(id1,name,pat_name,dept,date))
            print('Appointment Taken')
        elif choice==2:
             print('*'*50)
             print(' '*50)
             h= int(input('Enter patient id'))
             sql_w='delete from appointment where pat_id=({})'
             mycursor.execute(sql_w.format(h))
             print('Deletion done')

elif lv==4:
    while True:
        print('1. View appointments')
        print('2. View details of patient')
        print('3. Remove appointment')
        print('4. Exit')
        ch=int(input("enter choice"))
        if ch==1:
            print('*'*50)
            sql_w='select * from appointment'
            mycursor.execute(sql_w)
            s=mycursor.fetchall()
            for i in s:
                print(i)
                print("*"*50)
        elif ch==2:
            print('*'*50)
            h=(input("Enter patient ID or type 'all'for all the details "))
            if h=='all':
                print("*"*50)           
                sql_w='select * from patient'
                mycursor.execute(sql_w)
                s=mycursor.fetchall()
                for i in s:
                    print(i)
                    print("*"*50)
            else:
                sql_w='select * from patient where pat_id=("{}")'
                mycursor.execute(sql_w.format(h))
                s=mycursor.fetchall()
                for i in s:
                    print(i)
                    print('*'*50)
        elif ch==3:
            print('*'*50)
            h=input('Enter patient name')
            sql_w='delete from appointment where pat_name=({})'
            cl.execute(sql_w.format(h))
            print('Deletion done')

        elif ch==4:
            break
if lv==5:
    def Prepare_bill():
        pat_id=int(input("Enter patient id "))
        pat_name=input("Enter Patient name")
        bed=int(input("Enter Bed charges"))
        med=int(input("Enter Lab charges "))
        doc=int(input("Enter Doctor charges"))
        total=bed+med+doc
        mycursor.execute('insert into bill values({},"{}",{},{},{},{})'.format(pat_id,pat_name,bed,med,doc,total))
        print()
        print("*"*35)
        print(' '*10,'--BILL--')
        print()
        print('Patient ID     :     ',pat_id)                                                                        
        print('Patient name   :     ',pat_name)
        print("_"*20)
        print()
        print('Bed charge     :    Rs',bed)
        print('Lab charge     :    Rs',med)
        print('Doctors charge :    Rs',doc)
        print("-"*20)
        print('Total charge   :    Rs',total)
        print()
    Prepare_bill()
    print("*"*50)

if lv==6:
    print("*"*50)
              
    while True:
        print('1.Add record')
        print('2.display record')
        print('3. remove record')
        print('4.exit')
        c1=int(input("enter ch"))
        if c1==1:
            print("*"*50)
            lab_id=int(input("Enter lab id "))
            pat_id=int(input("Enter Patient id"))
            pat_name=input("Enter Patient name")
            age=int(input("Enter age "))
            test_type=input('Enter test type')
            Date=input("Enter date")
            ph=int(input("Enter phone no"))
            sq='insert into lab values({},{},{} "{}","{}","{}",{})'
            mycursor.execute(sq.format(lab_id,pat_id,pat_name,
            age,test_type,Date,ph))
            mydb.commit()
        elif c1==2:
            print("*"*50)
            h= input("Enter patient name or type 'all' for all the details ")
            if h=='all':
                print("*"*50)
                sql_w='select * from lab'
                mycursor.execute(sql_w)
                s=mycursor.fetchall()
                for i in s:
                    print(i)
                    print("*"*50)
                              
            else:
                sql_w='select * from lab where pat_name=("{}")'
                cl.execute(sql_w.format(h))
        elif ch==3:
            print("*"*50)
            h= int(input('Enter patient id'))
            sqlw='delete from lab where pat_name=("{}")'
            mycursor.execute(sqlw.format(h))
            print('Deletion done')
                       
        elif ch==4:
            break
