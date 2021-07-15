#interest calculation:

def interest_calculation(account_balance, calculation_time, interest_rate):      
    simple_interest = (account_balance * calculation_time * interest_rate)/100
    calc_amnt = account_balance*(pow((1 + interest_rate/100), calculation_time))
    compound_interest = calc_amnt - account_balance
      
    print('The Simple Interest is', simple_interest)
    return simple_interest
