while True :
    uname=input("Enter Username : ")
    if uname.upper() != "ADMIN" :
        print("Invalid username")
        break
    else :
        p=input("Enter password : ")
        if p != "BankManager" :
            print("Incorrect Password")
        else :
            print("Welcome")

            import pickle
            def Menu():
                print("*"*80)
                print(" "*30 , "Main Menu")
                print("*"*80)
                print("1. Insert Record/s")
                print("2. Display Records as per Account Number ")
                print("3. Delete Record ")
                print("4. Update Record ")
                print("5. Search Record details as per the account number ")
                #print("6. Search Record details as per Customer name")
                print("6. Debit withdraw from account ")
                print("7. Credit into an account")
                print("8. Logout")

            def SortAcc(a):
                try:
                    with open(a,'rb+') as q :
                        rec=pickle.load(q)
                        rec.sort(key=lambda rec:rec[0])
                        q.seek(0)
                        pickle.dump(rec,q)
                except FileNotFoundError :
                    print(a,"The file has no content")



            def SortName(a) :
                try :
                    with open(a,"rb+") as q:
                        Rec=pickle.load(q)
                        Rec.sort(key=lambda Rec:Rec[1])
                        q.seek(0)
                        pickle.dump(Rec,q)
                        print(Rec)
                except FileNotFoundError :
                    print(F,"The File has no records")


            def SortBal(a):
                try:
                    with open(a,"rb+") as q:
                        rec=pickle.load(q)
                        rec.sort(key=lambda rec:rec[7])
                        q.seek(0)
                        pickle.dump(rec,q)
                except FileNotFoundError:
                    print(a,"File has no records")

            def Insert(a):
                try:
                    q=open(a,"ab+")
                    print(q.tell())
                    if q.tell()>0:
                        q.seek(0)
                        Rec1=pickle.load(q)
                    else:
                        Rec1=[]
                    while True:
                        Acc=int(input("Enter account no: "))
                        Name=input("Enter Name: ")
                        Mob=int(input("Enter Mobile no: "))
                        email=input(input("Enter Email: "))
                        Add=input("Enter Address: ")
                        City=input("Enter City: ")
                        Country=input("Enter Country: ")
                        Bal=float(input("Enter Balance: "))
                        Rec=[Acc,Name.upper(),Mob,email.upper(),Add.upper(),City.upper(),Country.upper(),Bal]
                        Rec1.append(Rec)
                        print(Rec1)
                        q.close()
                        break
                    with open(a,"wb") as q:
                            pickle.dump(Rec1,q)
                except ValueError :
                    print("Invalid values entered")


            def Display(a):     #Function to Display the records in the Binary Files
                 try:
                      with open(a,"rb") as q:
                           print("="*75)
                           print("ACCNO","NAME","MOBILE","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","BALANCE",sep="\t")
                           print("="*75)
                           Rec=pickle.load(q)
                           c=len(Rec)
                           for i in Rec:
                                #for j in i:
                                    print(i,sep="")
                                    #print()
                           print("*"*75)
                           print("Records Read : ", c)
                           print("*"*75)

                 except EOFError:
                      print("*"*75)
                      print("Records Read : ", c ,end="\n")
                 except FileNotFoundError:
                      print(a , "File Doesn't exists ")


            def Delete(a):      #Function to delete the Record from the file, if it exists
                 try:
                      with open(a,"rb+") as q:
                           Rec=pickle.load(q)
                           ch=int(input("Enter the account number to be deleted: "))
                           for i in range(0,len(Rec)):
                                if Rec[i][0]==ch:
                                     print(Rec.pop(i))
                                     print("Record Deleted ")
                                     break
                           else:

                                print("Record not found")
                           q.seek(0)
                           pickle.dump(Rec,q)
                 except FileNotFoundError:
                      print(a,"File Doesn't exists")
                 except KeyError:
                      print("Record not found")
                 except IndexError:
                      print("Record not found")


            def Update(a):
                try:
                    with open(a,"rb+") as q :
                        Rec1=pickle.load(q)
                        f=-1
                        w=int(input("Enter the account number whose details to be changed : "))
                        for i in Rec1 :
                            if i[0]==w:
                                f=0
                                ch=input("Change Name (y/n) : ")
                                if ch=='y' or ch=="Y" :
                                    i[1]=input("Enter Name : ")
                                    i[1]=i[1].upper()

                                ch=input("change mobile number (y/n) : ")
                                if ch=='y' or ch=='Y' :
                                    i[2]=input("Enter Mobile number : ")

                                ch=input("Change Email (y/n) : ")
                                if ch=='y' or ch=="Y" :
                                    i[3]=input("Enter Email : ")
                                    i[3]=i[3].upper()

                                ch=input("Change Address (y/n) : ")
                                if ch=='y' or ch=="Y" :
                                    i[4]=input("Enter Address : ")
                                    i[4]=i[4].upper()

                                ch=input("Change city (y/n) : ")
                                if ch=='y' or ch=="Y" :
                                    i[5]=input("Enter city : ")
                                    i[5]=i[5].upper()

                                ch=input("Change Country (y/n) : ")
                                if ch=='y' or ch=="Y" :
                                    i[6]=input("Enter Name : ")
                                    i[6]=i[6].upper()

                                ch=input("Change Balance (y/n) : ")
                                if ch=='y' or ch=="Y" :
                                    i[7]=input("Enter Balance : ")
                                    i[7]=i[7].upper()


                            if f==-1:
                                print("Account details not found ")

                            else :
                                q.seek(0)
                                pickle.dump(Rec1,q)

                except EOFError :
                    print("Records read ",c)

                except FileNotFoundError :
                    print(a,"File doesn't exist")

            def SearchAcc(a):
                try:
                    with open(a,"rb") as q :
                        Rec=pickle.load(q)
                        ch=int(input("Enter the account number to be searched : "))
                        for i in range(0,len(Rec)):
                            if Rec[i][0]==ch:
                                print("="*75)
                                print("Account number","Name","Mobile","Email Address","Complete Address","City","Country","Balance")
                                print("="*75)
                                for j in Rec[i]:
                                    print(j,end='\t')
                                print()
                                break

                        else:
                            print("Record not found")
                except FileNotFoundError :
                    print(a,"File doesn't exists")

            def SearchName(a):
                try:
                    with open(a,"rb") as q :
                        Rec=pickle.load(q)
                        ch=input("Enter the Customer name to be searched : ")
                        for i in range(0,len(Rec)):
                            if Rec[i]==ch.upper():
                                print("="*75)
                                print("Account number","Name","Mobile","Email Address","Complete Address","City","Country","Balance")
                                print("="*75)
                                for j in Rec[i]:
                                    print(j,end='\t')
                                print()
                                break

                            else:
                                print("Record not found")
                except FileNotFoundError :
                    print(a,"File doesn't exists")


            def Debit(a):
                try:
                    with open(a,"rb+") as q :
                        Rec=pickle.load(q)
                        print("A minimum amount of Rs 1000 is to be maintained in the account for withdrawing the money ")
                        ac=int(input("Enter the account number : "))

                        for i in range(0,len(Rec)):
                            r=int(Rec[i][0])

                            if r ==ac :
                                m=int(input("Enter the amount to be withdrawn : "))
                                if r - m >1000 :
                                    r -= m
                                    print("Money is debited")
                                    break
                                else:
                                    print("Ther isn't the minimum balance in the account to withdraw money")
                                    break
                        else :
                            print("Record not found")
                        q.seek(0)
                        pickle.dump(Rec,q)

                except FileNotFoundError :
                    print(a,"File doesn't exists")


            def Credit(a):
                try:
                    with open(a,"rb+") as q :
                        Rec=pickle.load(q)
                        ac=int(input("Enter the account number : "))
                        for i in range(0,len(Rec)):
                            r=int(Rec[i][0])
                            if r ==ac :
                                am=int(input("Enter the amount to be credited : "))
                                r-=am
                                print("Money is credited")
                                break

                        else :
                            print("Record not found")
                        q.seek(0)
                        pickle.dump(Rec,q)

                except FileNotFoundError :
                    print(a,"File doesn't exists")


            Fi="Bank"
            while True :
                Menu()
                ch=int(input("Enter your choice : "))
                if ch==1 :
                    Insert(Fi)
                elif ch==2 :
                    SortAcc(Fi)
                    Display(Fi)
                elif ch==3 :
                    Delete(Fi)
                elif ch==4 :
                    Update(Fi)
                elif ch==5 :
                    SearchAcc(Fi)
                #elif ch==6 :
                    #SearchName(Fi)
                elif ch==7:
                    Debit(Fi)
                elif ch==8:
                    Credit(Fi)
                elif ch==9:
                    print("Exiting...")

                    break
                else:
                    print("Wrong Choice Entered")

