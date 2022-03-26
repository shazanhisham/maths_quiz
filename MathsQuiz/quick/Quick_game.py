def Quick():
        #Creating and assigning variables
        operand1=0
        operand2=0
        count=0
        result=0
        qnum=5
        
        #import 'random' for random operations
        import random

        #import 'mysql.connector' for databse operations
        import mysql.connector

        #Creating introduction
        print("\n",end="")
        print("----------Quick Game Play----------\n")
        print("You have 5 maths quize to Answer.\n")
        print("press ENTER after enter answers.\n")
        print("Let's start...")
             
        Player_name=(input("Enter your name : "))
        print("\n",end="")


        
        L1=[]#Create list L1
        for i in range(1,6):
                L2=[]#Create list L2
     
                operand1=(random.randint(0,10))
                L2.append(operand1)#append Operand1 to list L2
        
                operand2=(random.randint(0,10))
                L2.append(operand2)#append Operand2 to list L2
        
                print((str(i))+") ",operand1,"+",operand2,"=",end="")        
                user_answers=(input(" "))#Get user input answer
       
                L2.append(user_answers)#append user input answer to list L2
                L1.append(L2)#append list L2 to list L1

        #Results Introduction
        print("\n-----------Game Results-----------\n")
        print("Your name is",Player_name)
        print("\nYou answered "+str(len(L1))+" questions\n")

        #Checking user input answer with correct answer
        for i in range(len(L1)):
                print(str(i+1)+")",str(L1[i][0]),"+",str(L1[i][1]),"=",str(L1[i][2]),end="")
                ans = (L1[i][0]) + (L1[i][1])
                if str(ans)==(L1[i][2]):
                        print(" (answer" + str(ans) +") [Correct]")
                        count+=1
                else:
                        print(" (answer" + str(ans) +") [Incorrect]")
               

        #Results
        print("\nnumber of correct answers",count)
        result=int((count/5)*100)
        percentage=(str(result)+"%")
        print("youre score is",percentage,"\n")
        print("***end of the game***")

        
        #Open Database connection with a dictionery
        conDict={'host':'localhost',
                 'database':'math_quiz_game',
                 'user':'root',
                 'password':''}
        try:
                db=mysql.connector.connect(**conDict)
                print("Connection Successful\n")
                cursor = db.cursor()
                try:
                        mySQLtxt = "INSERT INTO player_result (Player_Name,Correct,Total_Quections,Percentage) VALUES (%s, %s, %s, %s)"
                        myValues = (Player_name,count,qnum,percentage)
                        cursor.execute(mySQLtxt,myValues)
                        db.commit()
                        print(cursor.rowcount,"Record added to Database\n")
                except:
                        print("Error occurs while inserting Data\n")
                db.close()
        except:
                print("Connection Fails\n")

      
     

        
