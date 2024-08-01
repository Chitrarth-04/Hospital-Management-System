import os
import pickle
import random

# New Patient Appointment .
def newpat():
    rec=[]
    pid=0
    if os.path.isfile('HMS.dat'):
        f=open('HMS.dat','rb')
        rec=pickle.load(f)
        f.close()
    nm=input('Enter Patient\'s Name :')
    age=int(input('Enter Patient\'s Age :'))
    gen=input('Enter Patient\'s Gender :')
    phn=int(input("Enter Phone No. :"))
    add=input("Enter Patient\'s Address :")
    dis=input('Enter Patient\'s Problem :')
    pid=len(rec)+1
    print("Your Patient's ID is : ",pid)
    print('Details Successfully Registered..')
    data=[pid,nm,age,gen,phn,add,dis]
    rec.append(data)
    a=random.randint(1,12)
    d=random.randint(1,31)
    e=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec']
    b=random.choices(e)
    c=str(d)+str(b)
    print("Your Date for the appointment is :",c,"2021")
    print("Your Time for the appointment is :",a,"PM")
    f=open('HMS.dat','wb')
    pickle.dump(rec,f)
    f.close()

# New Doctor Recruitment.    
def newdoc():
    rec=[]
    did=0
    if os.path.isfile('HMS1.dat'):
        f=open('HMS1.dat','rb')
        rec=pickle.load(f)
        f.close()
    nm=input('Enter Doctor\'s Name :')
    age=int(input('Enter Doctor\'s Age :'))
    gen=input('Enter Doctor\'s Gender :')
    phn=int(input("Enter Phone No. :"))
    add=input("Enter Doctor\'s Address :")
    dis=input('Enter Doctor\'s Qualification :')
    did=len(rec)+1
    print("Your Doctor's ID is : ",did)
    print('Details Successfully Registered..')
    data=[did,nm,age,gen,phn,add,dis]
    rec.append(data)
    a=random.randint(1,12)
    d=random.randint(1,31)
    e=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec']
    b=random.choices(e)
    c=str(d)+str(b)
    print("Your Date for the Interview is :",c,"2021")
    print("Your Time for the Interview is :",a,"PM")
    f=open('HMS1.dat','wb')
    pickle.dump(rec,f)
    f.close() 

# Showing Patient's Details : 
def showpat():
     print("\n1.Show All")
     print("2.Search")
     n=int(input("Enter Your Option : "))
     if n==1:
         f=open('HMS.dat','rb')
         rec=pickle.load(f)
         print('Patient\'s ID  \t  Name   \t\t  Age  \t  Gender  \t  Phone no. \t\t  Address  \t   Disease')
         print('===================================================================================')
         for i in rec:
             print(i[0], '\t\t' ,i[1],' \t\t ',i[2], '\t' ,i[3], '\t\t' ,i[4], '\t\t' ,i[5], '\t\t' ,i[6])
         f.close()
     elif n==2:
         n=int(input("Enter Patient's ID : "))
         if os.path.isfile('HMS.dat'):
             found=0
             f=open('HMS.dat','rb')
             rec=pickle.load(f)
             for i in rec:
                 if i[0]==n:
                     print('Patient\'s ID  \t  Name   \t\t  Age  \t  Gender  \t  Phone no. \t\t  Address  \t   Disease')
                     print('==================================================================================')
                     print(i[0], '\t\t' ,i[1],' \t\t ',i[2], '\t' ,i[3], '\t\t' ,i[4], '\t\t' ,i[5], '\t\t' ,i[6])
                     found=1
             f.close()
             if found==0:
                print("Record Not Found ")
         else:
             print("Record Does\'nt Exist")

# Showing Doctor's Details :
def showdoc():
     print("1.Show All")
     print("2.Search")
     n=int(input("Enter Your Option : "))
     if n==1:
         f=open('HMS1.dat','rb')
         rec=pickle.load(f)
         print('Doctor\'s ID  \t  Name   \t\t  Age  \t  Gender  \t  Phone no. \t\t  Address  \t   Qualification')
         print('====================================================================================')
         for i in rec:
             print(i[0], '\t\t' ,i[1],' \t\t ',i[2], '\t' ,i[3], '\t\t' ,i[4], '\t\t' ,i[5], '\t\t' ,i[6])
         f.close()
     elif n==2:
         n=int(input("Enter Doctor's ID : "))
         if os.path.isfile('HMS1.dat'):
             found=0
             f=open('HMS1.dat','rb')
             rec=pickle.load(f)
             for i in rec:
                 if i[0]==n:
                     print('Doctor\'s ID  \t  Name   \t\t  Age  \t  Gender  \t  Phone no. \t\t  Address  \t   Qualification')
                     print('====================================================================================')
                     print(i[0], '\t\t' ,i[1],' \t\t ',i[2], '\t' ,i[3], '\t\t' ,i[4], '\t\t' ,i[5], '\t\t' ,i[6])
                     found=1
             f.close()
             if found==0:
                print("Record Not Found ")
         else:
             print("Record Does\'nt Exist")
     
def update():
    print("1. Update Patient's Details ")
    print("2. Update Doctor's Details ")
    n=int(input("Enter your Option : "))
    
    # Updating Patient's Details :   
    if n==1:         
        f=open('HMS.dat','rb')
        rec=pickle.load(f)
        print('Patient\'s ID  \t  Name   \t\t  Age  \t  Gender  \t  Phone no. \t\t  Address  \t   Disease')
        print('====================================================================================')
        for i in rec:
            print(i[0], '\t\t' ,i[1],' \t\t ',i[2], '\t' ,i[3], '\t\t' ,i[4], '\t\t' ,i[5], '\t\t' ,i[6])
        f.close()
        print("1. Edit        2. Delete")
        m=int(input("Enter Your Option : "))

        # Editing :
        if m==1:
            if os.path.isfile("HMS.dat"):
                a=int(input("Enter Patien't ID to Edit : "))
                found=0
                f=open("HMS.dat",'rb')
                rec=pickle.load(f)
                for i in rec:
                    if i[0]==a:
                        print('Patient\'s ID  \t  Name   \t\t  Age  \t  Gender  \t  Phone no. \t\t  Address  \t   Disease')
                        print('===================================================================================')
                        print(i[0], '\t\t' ,i[1],' \t\t ',i[2], '\t' ,i[3], '\t\t' ,i[4], '\t\t' ,i[5], '\t\t' ,i[6])
                        found=1
                        newid=int(input("Enter New patient's ID : "))
                        newname=input("Enter New Name : ")
                        newage=int(input("Enter new age : "))
                        newgender=input("Enter New Gender : ")
                        newphn=int(input("Enter New Phone No. : "))
                        newadd=input("Enter New Address : ")
                        newdis=input("Enter New Disease : ")
                        newData=[newid,newname,newage,newgender,newphn,newadd,newdis]
                        rec[a-1]=newData
                        print("Details Succesfully Edited..")
                f.close()
                f=open("HMS.dat",'wb')
                pickle.dump(rec,f)
                f.close()
            else:
                print("No records to update...")

        # Deleting :
        elif m==2:
            if os.path.isfile("HMS.dat"):
                a=int(input("Enter Patien't ID to Delete : "))
                found=0
                f=open("HMS.dat",'rb')
                rec=pickle.load(f)
                for i in rec:
                    if i[0]==a:
                        print('Patient\'s ID  \t  Name   \t\t  Age  \t  Gender  \t  Phone no. \t\t  Address  \t   Disease')
                        print('===================================================================================')
                        print(i[0], '\t\t' ,i[1],' \t\t ',i[2], '\t' ,i[3], '\t\t' ,i[4], '\t\t' ,i[5], '\t\t' ,i[6])
                        found=1
                        rec.pop(a-1)
                        print("ID successfully Deleted...")
                f.close()
                f=open("HMS.dat",'wb')
                pickle.dump(rec,f)
                f.close()
            else:
                print("No records to Delete...")
                
    # Updating Doctor's Details :
    elif n==2:
        f=open('HMS1.dat','rb')
        rec=pickle.load(f)
        print('Doctor\'s ID  \t  Name   \t\t  Age  \t  Gender  \t  Phone no. \t\t  Address  \t   Qualification')
        print('====================================================================================')
        for i in rec:
            print(i[0], '\t\t' ,i[1],' \t\t ',i[2], '\t' ,i[3], '\t\t' ,i[4], '\t\t' ,i[5], '\t\t' ,i[6])
        f.close()
        print("1. Edit        2. Delete")
        m=int(input("Enter Your Option : "))

        # Editing :
        if m==1:
            if os.path.isfile("HMS1.dat"):
                a=int(input("Enter Doctor's ID to Edit : "))
                found=0
                f=open("HMS1.dat",'rb')
                rec=pickle.load(f)
                for i in rec:
                    if i[0]==a:
                        print('Doctor\'s ID  \t  Name   \t\t  Age  \t  Gender  \t  Phone no. \t\t  Address  \t   Qualification')
                        print('====================================================================================')
                        print(i[0], '\t\t' ,i[1],' \t\t ',i[2], '\t' ,i[3], '\t\t' ,i[4], '\t\t' ,i[5], '\t\t' ,i[6])
                        found=1
                        newid=int(input("Enter New Doctor's Id : "))
                        newname=input("Enter New Name : ")
                        newage=int(input("Enter new age : "))
                        newgender=input("Enter New Gender : ")
                        newphn=int(input("Enter New Phone No. : "))
                        newadd=input("Enter New Address : ")
                        newqua=input("Enter New Qualification : ")
                        newData=[newid,newname,newage,newgender,newphn,newadd,newqua]
                        rec[a-1]=newData
                        print("Details Succesfully Edited..")
                f.close()
                f=open("HMS1.dat",'wb')
                pickle.dump(rec,f)
                f.close()
            else:
                print("No records to update....")

        # Deleting :
        elif m==2:
            if os.path.isfile("HMS1.dat"):
                a=int(input("Enter Doctor's ID to Delete : "))
                found=0
                f=open("HMS1.dat",'rb')
                rec=pickle.load(f)
                for i in rec:
                    if i[0]==a:
                        print('Doctor\'s ID  \t  Name   \t\t  Age  \t  Gender  \t  Phone no. \t\t  Address  \t   Qualification')
                        print('===================================================================================')
                        print(i[0], '\t\t' ,i[1],' \t\t ',i[2], '\t' ,i[3], '\t\t' ,i[4], '\t\t' ,i[5], '\t\t' ,i[6])
                        found=1
                        rec.pop(a-1)
                        print("ID successfully Deleted...")
                f.close()
                f=open("HMS1.dat",'wb')
                pickle.dump(rec,f)
                f.close()
            else:
                print("No records to Delete...")

def Exit():
    print("*=====*=====*====May God Bless You======*======*=====*")
    exit(0)

# Menus
while True:
    print('\n\t\t===============================')
    print('\t\t\tWelcome To City Hospital')
    print('\t\t===============================')
    print('\t\t\t\tMenu')
    print('1. New Patient Appointment')
    print('2. New Doctor Recruitment')
    print("3. Show Patient's Details")
    print("4. Show Doctor's Details")
    print('5. Update Record')
    print('6. Exit')
    n=int(input('Enter your Option :'))
    if n==1:
        newpat()
    if n==2:
        newdoc()
    if n==3:
        showpat()
    if n==4:
        showdoc()
    if n==5:
        update()
    if n==6:
        Exit()
