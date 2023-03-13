import mysql.connector




def dosyaoku(filenamedf):#Txt read and process
    # Database Connection MYSQL
    connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database="databasename"
    )
    cncursor=connection.cursor()
    # Finish
    searchlist=[]
    with open(filenamedf,"r",encoding="utf-8") as file: #Open file and read("r")
        for satir in file: #satir = lines
            try:# If there is a ":" on the line, this part splits it up, otherwise ";" breaks down accordingly
                parser=satir.split(':')
                varpart=parser[1].strip('\n') # delete line skip character
                varpart2=parser[0]
            except:
                parser=satir.split(';')
                varpart=parser[1].strip('\n') # delete line skip character
                varpart2=parser[0]
                
            if [varpart2,varpart] in searchlist: #The same data entries are prevented by assigning the values to the list.
                pass
            else:
                searchlist.append([varpart2,varpart])
                # Add to Database
                sql="INSERT INTO tablename (column1,column2) VALUES (%s,%s)"
                variables=(varpart2,varpart)
                cncursor.execute(sql,variables)
                try:
                    connection.commit()
                except mysql.connector.Error as Err:
                    print("There is a Error: ",Err)

    connection.close()
    print("Mission Completed.CANMOSE")
                    


dosyaoku("filename.txt")