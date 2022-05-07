import sqlite3

cols=['Index', 'Number','Name', 'Special_species', 'Type_1', 'Type_2', 'Total', 'HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def', 'Speed']
pokemons_types=['Psychic', 'Fire', 'Electric', 'Steel', 'Ice', 'Fairy', 'Fighting', 'Grass', 'Flying', 'Water', 'Ground', 'Dragon', 
'Rock', 'Dark', 'Poison', 'Bug', 'None', 'Normal', 'Ghost']

conn=sqlite3.connect('pokemon_DB.db')
cursor=conn.cursor()

actcodeDESC="""
Welcome to Pokemons Dataset, Please select action code :

1 -- Search Pokemons by Type
2 -- Search Pokemons by Name (or Key words)
3 -- See how many Pokemons in each Type  
4 -- See how many Pokemons in each Species  
5 -- Search Top N Pokemons by specific column
6 -- Search Pokemons that whose specific column value higher than specific value
7 -- See average ability values by Type
8 -- According to the Pokemon you input, Search Pokemons that best to defeat it (calculate by Attack pros & cons / Defense pros & cons)
=================
0 -- Exit

"""

isrun=True
while isrun:
    actcode=input(actcodeDESC)
    if actcode=='1':
        cursor.execute("""
        select distinct Type_1 from `POKEMONS_DATABASE`;
        """)
        types1=cursor.fetchall()
        cursor.execute("""
        select distinct Type_2 from `POKEMONS_DATABASE`;
        """)
        types2=cursor.fetchall()

        types=list(set(types1).union(types2))
        all_types=[i[0] for i in types]

        type=input("Please input Pokemon type:\nTypes are {}\n".format(all_types))
        cursor.execute("""
        select * from `POKEMONS_DATABASE`
        where Type_1='{}' or Type_2='{}';
        """.format(type,type))
        records=cursor.fetchall()
        print(cols)
        for r in records:
            print(r)
        print("There are "+str(len(records))+" rows.")
    
    elif actcode=='2':
        pokemon_name=input("Please input the pokemon's name you want to search:\n")
        cursor.execute("""
        select * from `POKEMONS_DATABASE`
        where `Name` like "%{}%";
        """.format(pokemon_name))
        records=cursor.fetchall()
        print(cols)
        for r in records:
            print(r)
        print("There are "+str(len(records))+" rows.") 

    elif actcode=='3': 
        cursor.execute("""
        select Type_2, (coalesce(count_1,0)+count_2) as count from
        (select Type_2, count(*) as count_2 from `POKEMONS_DATABASE` group by Type_2) as Type_2
        left join 
        (select Type_1, count(*) as count_1 from `POKEMONS_DATABASE` group by Type_1) as Type_1 
        on Type_1.Type_1=Type_2.Type_2
        ;""")
        records=cursor.fetchall()
        for r in records:
            print(r)

    elif actcode=='4':
        cursor.execute("""
        select Special_Species, count(*) as count from `POKEMONS_DATABASE` group by Special_Species
        ;""")
        records=cursor.fetchall()
        for r in records:
            print(r)
    
    elif actcode=='5':
        column=input("Which column do you want to search for TOP N?\n(Total, HP, Attack, Defense, Sp_Atk, Sp_Def, Speed)\n")
        columns=[column]
        columns_top=['Total', 'HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def', 'Speed']
        
        while True:
            add_new_col=list(set(columns_top).difference(columns))
            more_cols=input("Any more columns? (Columns/No)\n{}\n".format(add_new_col))
            if more_cols.upper()!='NO':
                columns.append(more_cols)
                continue
            else:
                break
 
        top_n=int(input("How many number do you want to see the TOP?\n"))
        all_cols=input("Do you want to see all columns? (Yes/No)\n")
        
        if len(columns)>1:
            sql_cols_desc=''
            sql_cols=''
            for r in range(len(columns)):
                if r==len(columns)-1:
                    sql_cols_desc=sql_cols_desc+columns[r]+' desc '
                else:
                    sql_cols_desc=sql_cols_desc+columns[r]+' desc, '
                if r==len(columns)-1:
                    sql_cols=sql_cols+columns[r]
                else:
                    sql_cols=sql_cols+columns[r]+', '

            if all_cols.upper()=='NO':
                cursor.execute("""
                select `Number`, `Name`, `Special_species`, `Type_1`, `Type_2`, {} from `POKEMONS_DATABASE` order by {} limit {};
                """.format(sql_cols,sql_cols_desc,top_n))
                records=cursor.fetchall()
                print(['Number', 'Name', 'Special_species', 'Type_1', 'Type_2',sql_cols])
                for r in records:
                    print(r) 
            else:
                cursor.execute("""
                select * from `POKEMONS_DATABASE` order by {} limit {};
                """.format(sql_cols_desc,top_n))
                records=cursor.fetchall()
                print(cols)
                for r in records:
                    print(r)

        else:
            if all_cols.upper()=='NO':
                cursor.execute("""
                select `Number`, `Name`, `Special_species`, `Type_1`, `Type_2`, {} from `POKEMONS_DATABASE` order by {} desc limit {}
                ;""".format(column,column,top_n))
                records=cursor.fetchall()
                print(['Number', 'Name', 'Special_species', 'Type_1', 'Type_2','{}'.format(column)])
                for r in records:
                    print(r) 
            else:
                cursor.execute("""
                select * from `POKEMONS_DATABASE` order by {} desc limit {}
                ;""".format(column,top_n))
                records=cursor.fetchall()
                print(cols)
                for r in records:
                    print(r)

    elif actcode=='6':
        column=input("Which column do you want to search for?\n(Total, HP, Attack, Defense, Sp_Atk, Sp_Def, Speed)\n")
        value=input("Higher than what value?\n")
        cursor.execute("""
        select * from `POKEMONS_DATABASE` where `{}` > {}
        ;""".format(column,value))
        records=cursor.fetchall()
        print(cols)
        for r in records:
            print(r)        

    elif actcode=='7':  
        type=input("Please input Pokemon type:\nTypes are {}\n".format(pokemons_types))
        cursor.execute("""
        select round(avg(Total),2), round(avg(HP),2), round(avg(Attack),2), round(avg(Defense),2), round(avg(Sp_Atk),2), round(avg(Sp_Def),2), round(avg(Speed),2) 
        from `POKEMONS_DATABASE` 
        where `Type_1`='{}' or `Type_2`='{}'
        ;""".format(type,type))
        records=cursor.fetchall()
        print(['Total', 'HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def', 'Speed'])
        for r in records:
            print(r)    

    elif actcode=='8':
        pass

    elif actcode=='0':
        isrun=False
        
    else:
        print('PLEASE INPUT CORRECT ACTION CODE !')

cursor.close()
conn.close()