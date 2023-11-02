def solution():
    """On Tuesday, Liza had $800 in her checking account. On Wednesday, she paid her rent, $450. On Thursday, she deposited her $1500 paycheck. On Friday, she paid her electricity and internet bills which were $117 and $100, respectively. Then on Saturday, she paid her phone bill, $70. How much money is left in Liza's account?"""
    # Define Liza's starting balance and expenses
    starting_balance = 800
    rent = 450
    paycheck = 1500
    electricity_bill = 117
    internet_bill = 100
    phone_bill = 70

    # Calculate Liza's ending balance
    ending_balance = starting_balance - rent + paycheck - electricity_bill - internet_bill - phone_bill

    # Display Liza's ending balance
    result = ending_balance
    return result

print(solution())