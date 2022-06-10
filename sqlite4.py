#SQLITE4 DEVELOPED BY kute#0001
#BASED ON SQLITE3


import sqlite3 as sql
from colorama import Fore, init, Style
init(autoreset=True)

class database:
    def __init__(self):
        pass

    def new(self, name):
        self.name = name
        connection = sql.connect(f"{self.name}.db")
        connection.commit()
        connection.close()

    def table(self, tablename, table):
        try:

            table2 = []
            table = table.split(",")
            for i in table:
                ttype = ""
                k = i.replace(' ', '').split(':')
                if k[1] == "int": ttype = "integer"
                elif k[1] == "str": ttype = "text"
                j = f"{k[0]} {ttype},"
                table2.append(j)
            j2  = " ".join(table2)
            idx = f"CREATE TABLE {tablename} ({j2[:len(j2)-1]})"
            connection = sql.connect(f"{self.name}.db")
            cursor     = connection.cursor()
            cursor.execute(idx)
        except: pass

    def insert(self, tablename, insert):
        try:
            connection = sql.connect(f"{self.name}.db")
            cursor     = connection.cursor()
            idx        = f"INSERT INTO {tablename} VALUES ({insert})"
            cursor.execute(idx)
            connection.commit()
            connection.close()
        except: pass

    def select(self, tablename, argument, field=None, desc=False):
        connection = sql.connect(f"{self.name}.db")
        cursor     = connection.cursor()
        if desc == True: desc = "DESC"
        if desc == False: desc = ""
        idx = ""
        if field == None: idx = f"SELECT {argument} FROM {tablename}"
        if field != None: idx = f"SELECT {argument} FROM {tablename} ORDER BY {field} {desc}"
        cursor.execute(idx)
        data = cursor.fetchall()
        connection.commit()
        connection.close()
        return data

    def insertMany(self, tablename, argument):
        connection = sql.connect(f"{self.name}.db")
        cursor     = connection.cursor()
        idx        = f"INSERT INTO {tablename} VALUES (?, ?, ?)"
        cursor.executemany(idx, argument)
        connection.commit()
        connection.close()

    def search(self, tablename, argument, filter, method=None, field=None, desc=False):
        if desc == True: desc = "DESC"
        if desc == False: desc = ""
        connection = sql.connect(f"{self.name}.db")
        cursor     = connection.cursor()
        idx = ""
        filter = filter.split(":")
        if method == None and field == None: idx = f"SELECT {argument} FROM {tablename} WHERE {filter[0]} = '{filter[1]}'"
        if method == "like" and field == None: idx = f"SELECT {argument} FROM {tablename} WHERE {filter[0]} like '{filter[1]}'"
        if method == None and field != None: idx = f"SELECT {argument} FROM {tablename} WHERE {filter[0]} = '{filter[1]}' ORDER BY {field} {desc}"
        if method == "like" and field != None: idx = f"SELECT {argument} FROM {tablename} WHERE {filter[0]} like '{filter[1]}' ORDER BY {field} {desc}"
        if method == "<" or method == ">" or method == "=" or method == ">=" or method == "!=" or method == "<=":
            if field != None: idx = f"SELECT {argument} FROM {tablename} WHERE {filter[0]} {method} {filter[1]} ORDER BY {field} {desc}"
            else: idx = f"SELECT {argument} FROM {tablename} WHERE {filter[0]} {method} {filter[1]}"
        cursor.execute(idx)
        data = cursor.fetchall()
        connection.commit()
        connection.close()
        return data

    def update(self, tablename, objective, target, method=None):
        connection = sql.connect(f"{self.name}.db")
        cursor     = connection.cursor()
        objective  = "=".join(objective.split(":"))
        target     = target.split(":")
        if method == "like": idx        = f"UPDATE {tablename} SET {objective} WHERE {target[0]} like '{target[1]}'"
        if method == None: idx          = f"UPDATE {tablename} SET {objective} WHERE {target[0]}='{target[1]}'"
        cursor.execute(idx)
        connection.commit()
        connection.close()
    
    def delete(self, tablename, target, method=None):
        connection = sql.connect(f"{self.name}.db")
        cursor     = connection.cursor()
        target = target.split(":")
        if method == "like": idx        = f"DELETE FROM {tablename} WHERE {target[0]} like '{target[1]}'"
        if method == None: idx          = f"DELETE FROM {tablename} WHERE {target[0]}='{target[1]}'"
        cursor.execute(idx)
        connection.commit()
        connection.close()

def info():
    print(f"{Fore.RED}> {Style.BRIGHT}{Fore.GREEN}SQLite4 {Style.RESET_ALL}{Fore.RESET}developed by {Style.BRIGHT}{Fore.BLUE}kute#0001{Style.RESET_ALL}")
    print(f"{Fore.RED}> {Style.RESET_ALL}{Fore.RESET}Based on {Style.BRIGHT}{Fore.GREEN}SQLite3")
    print(f"{Fore.RED}> Note: {Style.RESET_ALL}{Fore.RESET}this {Style.BRIGHT}{Fore.GREEN}SQLite {Style.RESET_ALL}{Fore.RESET}version is not official and does not add new things, just modifies the syntax to make it easier")