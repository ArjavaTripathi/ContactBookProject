import sqlite3 
import re


delim = "4"

Add = str(input("Would you like to add a contact? Yes/No: "))
 
sqliteConnection = sqlite3.connect("contacts.db", isolation_level=None)

cursor = sqliteConnection.cursor()

def DeleteData(): 
    pass 




class Contacts: 
    def __init__(self, FirstName, LastName, Number): 
        self.FirstName = FirstName
        self.LastName = LastName
        self.Number = Number
    def AddContact(self, FirstName, LastName, Number):
        temp = [FirstName, LastName, Number] 
        
        res = dict()

        for idx, ele in enumerate(temp):
            res[idx] = ele


        print("Dictionary: " + str(res))

        cursor.execute('DROP TABLE IF EXISTS Data')

        sqlCreateTable = ''' CREATE TABLE IF NOT EXISTS Data (
                            id INTEGER PRIMARY KEY, 
                            FIRST_NAME TEXT(200) NOT NULL, 
                            LAST_NAME TEXT(200), 
                            NUMBER INTEGER

                    );'''

        cursor.execute(sqlCreateTable)

        value1 = res[0]
        value2 = res[1]
        value3 = res[2]

        params = (value1, value2, value3)

        sq1 = ''' INSERT INTO Data(FIRST_NAME, LAST_NAME, NUMBER) VALUES (?,?,?);''' 

        cursor.execute(sq1, params)
        sqliteConnection.commit()

        cursor.execute("SELECT * FROM Data")
        rows = cursor.fetchall()

        for rows in rows: 
            print(rows)
            print("Printed")
    def EditContact(self, FirstName, LastName, Number):
        cursor.execute("SELECT First_Name FROM Data") 
        d = cursor.fetchall()
        for d in d: 
            dlist = list(d)
            print(d)
            if d[0] == FirstName:
                DataChange = str(input("Would you like to change the FirstName, LastName or Number? (FirstName/LastName/Number): "))
                if DataChange == "FirstName": 
                    NameChange = str(input("What would you like to change the name to? "))
                    dlist[0] = NameChange
                    sq2 = '''UPDATE Data SET First_Name = (?) WHERE First_Name = (?);'''
                    param = (dlist[0], d[0])
                    cursor.execute(sq2, param)
                    sqliteConnection.commit()
                    cursor.execute("SELECT * FROM Data")
                    rows = cursor.fetchall()

                    for rows in rows: 
                        print(rows)
                        print("Printed")
                    


            elif d[0] != FirstName: 
                print("Not Found")
        



if Add == "Yes":
    global FirstName, LastName, Number 
    FirstName = str(input("What is the first name? "))
    LastName = str(input("What is the last name? "))
    Number = int(input("What is the number? "))
    Contacts(FirstName, LastName, Number)
    Contacts(FirstName, LastName, Number).AddContact(FirstName, LastName, Number)
elif Add == "No": 
    Edit = str(input("Would you like to edit a previous contact? Yes/No "))
    if Edit == "Yes":
        FirstName = str(input("What is the first name of the contact you would like to edit? "))
        LastName = str(input("What is the last name of the contact you would like to edit? "))
        Contacts(FirstName, LastName, Number = None).EditContact(FirstName, LastName, Number = None)
