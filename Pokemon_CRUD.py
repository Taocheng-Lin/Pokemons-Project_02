import  sqlite3


conn=sqlite3.connect('pokemon_DB.db')
cursor=conn.cursor()

appDesc="""
Please input action code :

1 -- Insert Data
2 -- Update Data
3 -- Delete Data 
4 -- Retrieve All Data
=================
0 -- Exit

"""
isRun=True
while isRun:
    ctrl=input(appDesc)
    if ctrl=="0":
        isRun=False
    
    elif ctrl=="1":
        Number=int(input('Please input Number:\n'))
        Name=input('Please input Name:\n')
        Special_Species=input('Please input Special_Species:\n')
        Type_1=input('Please input Type_1:\n')
        Type_2=input('Please input Type_2:\n')
        HP=int(input('Please input HP:\n'))
        Attack=int(input('Please input Attack:\n'))
        Defense=int(input('Please input Defense:\n'))
        Sp_Atk=int(input('Please input Sp_Atk:\n'))
        Sp_Def=int(input('Please input Sp_Def:\n'))
        Speed=int(input('Please input Speed:\n'))
        Total=HP+Attack+Defense+Sp_Atk+Sp_Def+Speed
        sql="""
        INSERT INTO `POKEMONS_DATABASE`(Number,Name,Special_Species,Type_1,Type_2,
        Total,HP,Attack,Defense,Sp_Atk,Sp_Def,Speed)
        VALUES ({},'{}','{}','{}','{}',{},{},{},{},{},{},{});
        """.format(Number,Name,Special_Species,Type_1,Type_2,Total,HP,Attack,Defense, Sp_Atk, Sp_Def, Speed)
        cursor.execute(sql)
        conn.commit()
        cursor.execute("""
        select * from `POKEMONS_DATABASE`
        order by `Index` desc
        limit 1;
        """)
        records=cursor.fetchall()
        print(records)
    
    elif ctrl=="2":
        update_row=input("Please input THE INDEX OF ROW you want to UPDATE:\n")
        cols_chra=['HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def', 'Speed']
        col=input("Please input the column you want to update:\nCOLUMNS: Number, Name, Special_Species, Type_1, Type_2, HP, Attack, Defense, Sp_Atk, Sp_Def, Speed (Once a time)\n")
        value_update=input("Please input the UPDATE value:\n")
        dif=0
        if col in cols_chra:
            cursor.execute("select {} from POKEMONS_DATABASE where `Index`={};".format(col,update_row))
            records=cursor.fetchall()
            dif=int(value_update)-records[0][0]
        sql="""
        update POKEMONS_DATABASE set {}='{}',Total=Total+{}
        where `Index`={};
        """.format(col,value_update,dif,update_row)
        cursor.execute(sql)
        conn.commit()
        cursor.execute("select * from POKEMONS_DATABASE where `Index`={};".format(update_row))
        records=cursor.fetchall()
        print('The row is updated:\n',records)

    elif ctrl=="3":
        delete_row=int(input("Please input THE INDEX OF ROW you want to DELETE:\n"))
        sql="""
        DELETE FROM `POKEMONS_DATABASE`
        WHERE `Index`={};
        """.format(delete_row)
        cursor.execute("""select * from POKEMONS_DATABASE where `Index`={};""".format(delete_row))
        records=cursor.fetchall()
        cursor.execute(sql)
        conn.commit()
        print("The row you deleted:\n",records)
    
    elif ctrl=="4":
        cursor.execute("""
        select * from POKEMONS_DATABASE;
        """)
        records=cursor.fetchall()
        for r in records:
            print(r)
    else:
        print('PLEASE INPUT CORRECT ACTION CODE !')


cursor.close()
conn.close()