#customer actions (deposit and withdraw): 
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


#deposit amount to customer's account:
def custom_deposit(amount):
    acc_num = int(input("Enter your account number: "))
    var_cursor.execute("select account_balance from bank where account_number=?",(acc_num,))
    bal=var_cursor.fetchall()
    bal=bal[0][0]
    new_bal=bal+int(amount)

    var_cursor.execute("update bank set account_balance=? where account_number=?",(new_bal,acc_num))
    var_connect.commit()

#withdraw amount from customer's account
def custom_withdraw(amount,account_number):
    acc_num = int(input("Enter your account number: "))
    var_cursor.execute("select account_balance from bank where account_number=?",(acc_num,))
    bal=var_cursor.fetchall()
    bal=bal[0][0]
    if bal<int(amount):
        return False
    else:
        new_bal=bal-int(amount)

        var_cursor.execute("update bank set account_balance=? where account_number=?",(new_bal,acc_num))
        var_connect.commit()
        return True

connect_database()
print("Added 120:",custom_deposit(120))
