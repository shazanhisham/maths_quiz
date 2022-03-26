def delete_results():
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
    cursor.execute("DELETE FROM player_result")

    #Commit the change
    db.commit()
    print("All record deleted")
    
    #Disconnect from server
    db.close()

    
