from decimal import ROUND_05UP
import sqlite3

from colorama import Cursor

conn=sqlite3.connect('pokemon_DB.db')
cursor=conn.cursor()

type=input("Please input Pokemon type:\n")
cursor.execute("""
select * from `POKEMONS_DATABASE`
where Type_1='{}' or Type_2='{}';
""".format(type,type))
records=cursor.fetchall()

for r in records:
    print(r)
print("There are "+str(len(records))+" rows.")

cursor.execute("""
select distinct Type_1 from `POKEMONS_DATABASE`;
""")
types1=cursor.fetchall()
cursor.execute("""
select distinct Type_2 from `POKEMONS_DATABASE`;
""")
types2=cursor.fetchall()
print(types1)
types=[]
for i in types1:
    types.append(i[0])

print(types)


cursor.close()
conn.close()