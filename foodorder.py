import mysql.connector
#Create the connection object
myconn = mysql.connector.connect(host="127.0.0.1", user="root", passwd="",database="db1")


cur = myconn.cursor()

try:
    #Creating a tables=> Food , orders . 
    dbs = cur.execute("create table Food(ID int(20) not null primary key, Name varchar(20) not null,Price int(20) not null)")
    dbs2 = cur.execute("create table Orders(CustName varchar(20) not null,Items varchar(20) not null,Bill int not null)")

    #Insert Operation For Food Table
    sql = "insert into Food(ID,Name,Price) values (%s, %s, %s)"

    # The row values are provided in the form of tuple
    row1 = (1,"Burger",50)
    row2 = (2,"Pizza", 100)
    row3 = (3,"Fries", 80)
    row4 = (4,"Cold coffee", 40)
    row5 = (5, "Tea", 20)
    row6 = (6, "Cold Drink", 30)
   

    # inserting the values into the Food table. 
    cur.execute(sql, row1)
    cur.execute(sql, row2)
    cur.execute(sql, row3)
    cur.execute(sql, row4)
    cur.execute(sql, row5)
    cur.execute(sql, row6)
   
    # commit the transaction
    myconn.commit()

except:
     myconn.rollback()


print("Welcome to the Swati's_Resto ! ")
print("")

cname=input("May I know your Good name plz:   ")
print("")

print("Select your food from the menu")
try:

    cur.execute("select * from food")
    Records = cur.fetchall()

    print("ID", "Name", "Price")
    for i in Records:
        print(i)
except:
    print("error")

b="yes"
orderlist=[]
while (b!="no"):
    order = input("Enter your food:  ")
    orderlist.append(order)
    b=input("Enter 'no' to complete the list and get the bill or 'yes' to add more: ")


bill=0
try:
    cur.execute("select * from food")
    Records = cur.fetchall()
    for j in orderlist:
        for rc in Records:
            if j==str(rc[1]):
                bill+=int(rc[2])

    print("Your Order has been placed! ")
    tip = int(input("Enter any Tip for the Rider :"))
    bill+=tip+20
    print("")
    print("")
    print("Delivery Charges = 20")
    print("")
    print("")
    print("")
    print("Total Bill = "+ str(bill))
    print("Thank You for order \U0001F600 . \n Your order will be delivered soon \U0001F618 \n Stay home Stay safe \U0001F637")
    
except:
    print("error")


#Insert operation in Order table
sql2 = "insert into Orders(CustName,Items,Bill) values (%s,%s,%s)"
row=(cname,str(orderlist),str(bill))
cur.execute(sql2, row)
myconn.commit()

#Display order history
print("Order History")
cur.execute("select * from Orders")
Records = cur.fetchall()

print("CustName", "Items","Bill")
for i in Records:
    print(i)


myconn.close()

