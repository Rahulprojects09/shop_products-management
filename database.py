import pymysql

con = None
cursor = None

def dbconnect():
    global con, cursor
    con = pymysql.connect(host='localhost',
                    user='root',
                    password='',
                    database='shop')
    cursor = con.cursor()    

def dbdisconnect():
    cursor.close()
    con.close()

def insertrecord(Id,BrandName,ProductName,EntryDate,StockKg,PriceKg,Discount,FinalPrice):
    dbconnect()
    query = f'insert into products values({Id},"{BrandName}","{ProductName}",{EntryDate},{StockKg},{PriceKg},{Discount},{FinalPrice})'
    cursor.execute(query)
    con.commit()
    dbdisconnect()

def readall():
    dbconnect()
    query = 'select * from products'
    cursor.execute(query)
    data = cursor.fetchall()
    #print(data)
    dbdisconnect()
    return data

def readbyid(Id):
    dbconnect()
    query = f'select * from products where Id={Id}'
    cursor.execute(query)
    data = cursor.fetchone()
    dbdisconnect()
    return data

def updaterecord(data):
    dbconnect()
    query = f'update products set BrandName="{data[1]}",ProductName="{data[2]}",EntryDate="{data[3]}",StockKg="{data[4]}",PriceKg="{data[5]}",Discount="{data[6]}",FinalPrice="{data[7]}" where id={data[0]}'
    cursor.execute(query)
    con.commit()
    dbdisconnect()

def deleterecord(Id):
    dbconnect()
    query = f'delete from products where Id={Id}'
    cursor.execute(query)
    con.commit()
    dbdisconnect()