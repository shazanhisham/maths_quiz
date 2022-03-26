def past_results():
    import mysql.connector

    #Open database connection with a dictionery

    conDict = {'host':'localhost',
               'database':'Math_quiz_game',
               'user':'root',
               'password':''}

    db=mysql.connector.connect(**conDict)

    #Prepare a cursor object using cursor() method
    cursor=db.cursor()

    #Execute SQL query using execute() method.
    cursor.execute("SELECT * FROM player_result")

    #Fetch results using fetchall() method.
    data=cursor.fetchall()

    #Creating table
    Heading=("| Player Name |Correct|Total_Questions|Percentage|")
    print("-"*len(Heading))
    print(Heading)
    print("-"*len(Heading))

    for item in data:
        print("|",item[0]," "*int(10-len(item[0])),
              "|",item[1]," "*int(4-len(item[1])),
              "|",item[2]," "*int(12-len(item[2])),
              "|",item[3]," "*int(7-len(item[3])),
              "|")
        print("-"*len(Heading))
    #Disconnect from server
    db.close()

    
