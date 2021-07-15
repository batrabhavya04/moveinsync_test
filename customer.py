#customer actions (deposit and withdraw): 

#deposit amount to customer's account:
def custom_deposit(amount,account_number):
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
