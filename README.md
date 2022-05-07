# Pokemons-Project
Pokemons Dataset searcher


# 專案目標： 
1. 從 https://pokemondb.net/pokedex/all 爬取公開資料
2. 將原始資料前處理，並儲存成CSV檔，創建SQL資料庫及資料表，用SQLite存儲資料
3. 使用SQLite對資料進行CRUD，讓管理者能輕鬆修改、新增、查詢或刪除寶可夢資料，並使用DB Browser(SQLite)管理資料庫
4. 透過操作SQL查詢語法，讓使用者可以根據不同功能查詢寶可夢資料，目前功能如下:
    1 -- Search Pokemons by Type
    2 -- Search Pokemons by Name (or Key words)
    3 -- See how many Pokemons in each Type  
    4 -- See how many Pokemons in each Species  
    5 -- Search Top N Pokemons by specific column
    6 -- Search Pokemons that whose specific column value higher than specific value
    7 -- See average ability values by Type
    8 -- According to the Pokemon you input, Search Pokemons that best to defeat it (calculate by Attack pros & cons / Defense pros & cons)(開發中)
5.包裝join、group by、子查詢等SQL語法，讓使用者能輕鬆查詢寶可夢資料


# 未來優化方向:
1.可同時查詢多欄位大於指定數值的寶可夢(search檔案功能6)
2.新增寶可夢克制查詢功能(search檔案功能8)
3.優化使用者輸入錯誤資料時的回應方式
4.資料視覺化


# 使用技術： Python, SQLite


# 實際運行

## 爬蟲
![image](https://user-images.githubusercontent.com/103302287/167241001-32b05dde-e490-41a9-9234-e94a16bc515c.png)

## 資料前處理
![image](https://user-images.githubusercontent.com/103302287/167240978-0b10b246-98c9-4eb3-b64c-2e7ec3db232e.png)

資料庫SQL增刪改查
![image](https://user-images.githubusercontent.com/103302287/167241738-c9ba7f02-5f9f-4bae-b961-17f9099004b3.png)

查詢資料庫的寶可夢資料
![image](https://user-images.githubusercontent.com/103302287/167242580-7a4ce4d2-525b-4bc3-8c95-14478c618409.png)




