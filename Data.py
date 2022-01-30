from multiprocessing import connection
import sqlite3 
import sys

connection = sqlite3.connect("people.db")

cursor = connection.cursor()

try:
    cursor.execute("CREATE TABLE people(name TEXT, age INTEGER, skills STRING)")

except Exception as e:
    pass

def user_is_unique(name):
    rows = cursor.execute("SELECT name, age, skills FROM people").fetchall()

    for user in rows:
        if user[0] == name:
            return False
    return True


def insert_db():
    name = input("Name>>")

    if user_is_unique(str(name)):
        age = input("Age>>")
        skills = input("Skill>>")

        if name != "" and age != "" and skills != "":
            cursor.execute(f"INSERT INTO people VALUES ('{name}, {age}, {skills}')")
            connection.commit()
            print(name + " has been added tot the database!")

        else:
            print("One of the fields are empty! Please try again!")
            insert_db()
    else:
        print("The name is already in the databases")


def modify_db():
    name = input("Type the name of the person you'd like to edit >>")
    field = input("Which field would you like to edit: name, age or skills ? >>")
    update_field = input("What would you like to update it to >>")

    try:   
        cursor.execute(f"UPDATE people SET {field} = ? WHERE name = ?", (update_field, name))
        connection.commit()
        print("Successfully updated!")


    except Exception as e:
        print(e)

def get_user_info_db():
    target_name = input("who do you want to see information about? >>")
    rows = cursor.execute ("SELECT name, age, skills FROM people WHERE name = ?", (target_name)).fetchall

    try:
        connection.commit()
        print("This is the user >>")

    except Exception as e:
        print(e)

