#manager role:

import sqlite3

#making connection with database
def connect_database():
    global var_connect
    global var_cursor
    var_connect = sqlite3.connect("moveinsynctest.db")

    var_cursor = var_connect.cursor()

    var_cursor.execute(
        "create table if not exists bank (account_number int, customer_name text, customer_age int, customer_address text, account_balance int, account_type text, mobile_number int)")
    var_cursor.execute("create table if not exists admin (customer_name text, pass text)")
    var_cursor.execute("insert into admin values('bhavya','987')")
    var_connect.commit()
    var_cursor.execute("select account_number from bank")
    acc = var_cursor.fetchall()
    global account_number
    if len(acc) == 0:
        account_number = 1
    else:
        account_number = int(acc[-1][0]) + 1

#check admin dtails in database
def check_admin(customer_name,password):

    var_cursor.execute("select * from admin")
    data=var_cursor.fetchall()

    if data[0][0]==customer_name and data[0][1]==password:
        return True
    return

#adding customer in database
def add_customer(customer_name,customer_age,customer_address,account_balance,acc_type,mobile_number):
    global account_number
    var_cursor.execute("insert into bank values(?,?,?,?,?,?,?)",(account_number,customer_name,customer_age,customer_address,account_balance,acc_type,mobile_number))
    var_connect.commit()
    account_number=account_number+1
    return account_number-1

#check account in database
def check_account_number(account_number):
    var_cursor.execute("select account_number from bank")
    list_account_number=var_cursor.fetchall()

    print("List of all accounts: ",[i[0] for i in list_account_number])
    for i in range(len(list_account_number)):
        if list_account_number[i][0]==int(account_number):
            return True
    return False

#get all details of a particular customer from database
def get_details(account_number):
    var_cursor.execute("select * from bank where account_number=?",(account_number))
    global detail
    detail = var_cursor.fetchall()
    print(detail)
    if len(detail)==0:
        return False
    else:
        return (detail[0][0],detail[0][1],detail[0][2],detail[0][3],detail[0][4],detail[0][5],detail[0][6])

#add new amount to customer's account in bank database
def update_balance(amount,account_number):
    var_cursor.execute("select account_balance from bank where account_number=?",(account_number,))
    bal=var_cursor.fetchall()
    bal=bal[0][0]
    new_bal=bal+int(amount)

    var_cursor.execute("update bank set account_balance=? where account_number=?",(new_bal,account_number))
    var_connect.commit()

#deduct amount from customer's account in bank database
def deduct_balance(amount,account_number):
    var_cursor.execute("select account_balance from bank where account_number=?",(account_number,))
    bal=var_cursor.fetchall()
    bal=bal[0][0]
    if bal<int(amount):
        return False
    else:
        new_bal=bal-int(amount)

        var_cursor.execute("update bank set account_balance=? where account_number=?",(new_bal,account_number))
        var_connect.commit()
        return True

#account_balance of a particular account number from database
def check_balance(account_number):
    var_cursor.execute("select account_balance from bank where account_number={}".format(account_number))
    bal=var_cursor.fetchall()
    return bal[0][0]

#update_name_in_bank_table
def update_name_in_bank_table(new_name,account_number):
    print(new_name)
    var_connect.execute("update bank set customer_name='{}' where account_number={}".format(new_name,account_number))
    var_connect.commit()

#update_age_in_bank_table
def update_age_in_bank_table(new_name,account_number):
    print(new_name)
    var_connect.execute("update bank set customer_age={} where account_number={}".format(new_name,account_number))
    var_connect.commit()

#update_address_in_bank_table
def update_address_in_bank_table(new_name,account_number):
    print(new_name)
    var_connect.execute("update bank set customer_address='{}' where account_number={}".format(new_name,account_number))
    var_connect.commit()

#list of all customers in bank
def list_all_customers():
    var_cursor.execute("select * from bank")
    lst_customer=var_cursor.fetchall()
    return lst_customer
    
#delete account from database
def delete_customer(account_number):
    var_cursor.execute("delete from bank where account_number=?",(account_number))
    var_connect.commit()

#get customer_name and account_balance from bank of a particular account number
def get_detail(account_number):
    var_cursor.execute("select customer_name, account_balance from bank where account_number=?",(account_number))
    details=var_cursor.fetchall()
    return details

connect_database()
x=''
while(x!='q'):
    print(check_account_number(1))
    print("1: List all Accounts")
    print("2: Add Customer: 2")
    print("3: Check if account exists: 3")
    print("4: Exit: q")
    x=input("Enter choice: ")
    print('\n\n\n')
    print("---------------------")
    if(x=="1"):
        for i in (list_all_customers()):
            print(list(i))
    if(x=="2"):
        customer_name=input("Enter customer_name: ")
        customer_age=input("Enter customer_age: ")
        customer_address=input("Enter customer_address: ")
        acc_type=input("Enter acc_type: ")
        mobile_number=int(input("Enter mobile_number: "))

        add_customer(customer_name,customer_age,customer_address,acc_type,0,mobile_number)
    if(x=="3"):
        account_number = int(input("account_number"))
        check_account_number(account_number)
    print('\n\n\n')
    print("---------------------")
