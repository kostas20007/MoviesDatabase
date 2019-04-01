import sqlite3
import os
clear = lambda: os.system('cls')
conn = sqlite3.connect("Movies.db")
conn.execute('''CREATE TABLE IF NOT EXISTS NAMES(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
NAME text NOT NULL,YEAR text NOT NULL)''')


def menu():
    clear()
    print("MOVIES - MAIN MENU")
    print("--------------------")
    print("1. Search Movie")
    print("2. Enter New Movie")
    print("3. View All Movies")
    print("4. Delete Movie")
    print("5. Edit Movie")
    print("6. Exit")
    cho=input("Enter your choice: ")
    if cho=='1':
        search()
    elif cho=="2":
        enterNew()
    elif cho=="3":
        printAll()
    elif cho=="4":
        delete()
    elif cho=="5":
        edit()    
    else:
        bye()

def search():
    clear()
    print("MOVIES - SEARCH")
    print("-----------------")
    cho=input("Enter title or year of the movie, please: ")
    choUp=cho.upper()
    
    cursor = conn.execute("SELECT * FROM NAMES WHERE upper(NAME) GLOB '*%s*' \
    OR upper(YEAR) GLOB '*%s*' ORDER BY YEAR ASC" % (choUp,choUp))
    

    view(cursor)
       
       
    
    input("\nPress Enter for Menu")
    menu()   

    

def enterNew():
    clear()
    print("MOVIES - ENTER NEW")
    print("--------------------")
    n=""
    y=""
    
    while len(n) < 1:

        n=input("Enter Title of movie: ")
        
            
    while len(y) < 1:
        y=input("Enter Year of movie: ")

   
                 
   
    conn.execute("INSERT OR IGNORE INTO NAMES(NAME,YEAR)  \
    VALUES (?,?)",[n,y])
    conn.commit()
    print("\nSuccess!!!")
    input("Press Enter for Menu")
    
    menu()    




def printAll():
    clear()
    print("MOVIES - VIEW ALL")
    print("--------------------")
       
    
    cursor = conn.execute("SELECT * FROM NAMES")

    view(cursor)    
         
    input("\nPress Enter for Menu")
    menu()
def bye():
    conn.close()
    input("Press Enter to exit!!!")

def delete():
    clear()
    print("MOVIES - DELETE MOVIE")
    print("--------------------")
    
    idcon=input("Enter the ID of the Movie you want to delete: ")
    vals = conn.execute("SELECT * FROM NAMES WHERE ID=?", [idcon]).fetchone()
    if vals:
        cursor = conn.execute("SELECT * FROM NAMES WHERE ID = ?" ,[idcon])
        view(cursor)
        ans=input("Delete this movie? (y/n)")
        if ans.upper()=="Y":
         
            conn.execute("DELETE FROM NAMES WHERE ID = ?",[idcon])
            conn.execute("Delete from sqlite_sequence where name='NAMES'")
            print("Deleted")
            callMenu(conn)
        
        else:
            input("Deletion Canceled. Press Enter for Menu")
            
            menu()
            
    else:
        
        input("\nMovie not found. Press Enter for Menu")
        menu()

        
    
def edit():
    clear()
    print("MOVIES - EDIT")
    print("--------------------")
    
    
    idcont=input("\nEnter the ID of the Movie you want to edit: ")
    vals = conn.execute("SELECT * FROM NAMES WHERE ID=?", [idcont]).fetchone()
    
    if vals:
        cursor = conn.execute("SELECT * FROM NAMES WHERE ID = ?" ,[idcont])
        view(cursor)
        el=""
        print("\nWhat do you want to do?")
        element = input("\n1.Edit ID\n2.Edit Title\n3.Edit Year\n4.Return to Menu\n")
        if element=='1':
            idnew=""
            while not idnew.isdigit():
                idnew=input("Enter the new ID for the movie: ")
            vals2 = conn.execute("SELECT * FROM NAMES WHERE ID=?", [idnew]).fetchone()
            if vals2:
                print("The ID already exists")
                
                input("Press Enter for Menu")
                menu()
            else:
                conn.execute("UPDATE NAMES set ID = ? where ID = ?",[idnew,idcont])
                print("ID changed")
                callMenu(conn)
        elif element=='2':
            nameNew=input("Enter new Title for the movie: ")
            conn.execute("UPDATE NAMES set NAME = ? where ID = ?",[nameNew,idcont])
            print("Title of the Movie has changed")
            callMenu(conn)
                
        elif element=='3':
            yearNew=input("Enter new Year for the movie: ")
            conn.execute("UPDATE NAMES set YEAR = ? where ID = ?",[yearNew,idcont])
            print("Year of the movie has changed")
            callMenu(conn)
        
        elif element=='4':
            
            menu()
        else:
            print("Wrong Input")
            input("Press Enter for Menu")
            menu()
            
    else:
        input("Movie does not exist. Press Enter for Menu")
        
        menu()
    
def callMenu(conn):
    conn.commit()
    
    input("Press Enter for Menu")
    menu()

    

def view(cursor):
    for row in cursor:
       print ("\nID    = ", row[0]) 
       print ("TITLE = ", row[1])
       print ("YEAR  = ", row[2])
       
  

    
    
menu()
