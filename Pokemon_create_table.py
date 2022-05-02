import sqlite3
import csv

conn=sqlite3.connect('pokemon_DB.db')
cursor=conn.cursor()
#創建資料表
cursor.execute("drop table POKEMONS_DATABASE")
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS "POKEMONS_DATABASE" (
	"Index"	INTEGER NOT NULL,
	"Number"	INTEGER,
	"Name"	TEXT,
	"Special_Species"	TEXT,
	"Type_1"	TEXT,
	"Type_2"	TEXT,
	"Total"	INTEGER,
	"HP"	INTEGER,
	"Attack"	INTEGER,
	"Defense"	INTEGER,
	"Sp_Atk"	INTEGER,
	"Sp_Def"	INTEGER,
	"Speed"	INTEGER,
	PRIMARY KEY("Index")
);
""")

with open('./data/pokemons.csv','r',encoding='utf-8') as file:
	# 觀察資料
	# root=file.read()
	# rows=csv.DictReader(file)
	# for row in rows:
	# 	print(row)
		#for x in row.items():
		#	print(x)

	rows=csv.reader(file)
	headers=next(rows)
	print("Headers: %s" % headers)
	for row in rows:
		cursor.execute("INSERT INTO `POKEMONS_DATABASE` VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);",[
				int(row[0]),int(row[1]),row[2],row[3],row[4],row[5],int(row[6]),int(row[7]),
				int(row[8]),int(row[9]),int(row[10]),int(row[11]),int(row[12]),
		])
	conn.commit()


# 刪除資料表
# cursor.execute("""  
# DROP TABLE 'test';
# """)

# 用SQL讀取資料
cursor.execute("""
select * from POKEMONS_DATABASE
""")
records=cursor.fetchall()
print(type(records))
for i in records:
    print(i)

cursor.close
conn.close