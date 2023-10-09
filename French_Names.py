import random
import mysql.connector

mydb = mysql.connector.connect(
 host= "localhost",
 user= "root",
 password= "",
 database= "french_people"
)

mycursor = mydb.cursor()


mNames = ["Pierre", "Claude", "Jean", "Paul"]

fNames = ["Claire", "Marie", "Simone", "Elise"]

lNames= ["de Chartes", "Duclare", "Dupuis", "Dupont", "Jospin"]


def secondTry():
    answer = input("Try again? y/n \n")
    if(answer.lower() == "y" or answer.lower() == "yes"):
        ask()
    elif(answer.lower() == "n" or answer.lower() == "no"):
        print("goodbye")
    else:
        print("I did not get that.")
        secondTry()
        #this is bugged for some reason.

def makeName(gender):
    firstName = random.choice(gender)
    middleName = random.choice(gender)

    if(firstName == middleName):
        makeName(gender)
    else:
        newName = firstName + "-" + middleName + " " + random.choice(lNames)
        print(newName)
        #we are pre-assigning the male gender for simplification
        table = "female"
        if(gender == mNames):
            table = "male"
        databaseQ(newName, table)
        secondTry()
    

       
def databaseQ(newName, table):
    answer = input("Would you like to add this name to the database?")
    if(answer.lower() == "y" or answer.lower() == "yes"):
        #this statement below, specifically the second part, seems to give an error.  Why?
        sql = "INSERT INTO " + table + " (name) VALUES ('" + str(newName) + "');"
        mycursor.execute(sql)
        mydb.commit()
        print("Name added")
    elif(answer.lower() == "n" or answers.lower() == "no"):
        print("Name not added")
    else:
        print("I did not get that.")
        databaseQ(gender, newName)
    
def ask():
    choice = input("Male or female \n")
    if(choice.lower() == "male" or choice.lower() == "m"):
        makeName(mNames)
    elif(choice.lower() == "female" or choice.lower() == "f"):
        makeName(fNames)
    else:
        print("sorry, didn't get that")
        ask()


ask()
