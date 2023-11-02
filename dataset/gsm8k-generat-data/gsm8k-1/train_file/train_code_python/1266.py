def solution():
    """On Tuesday, Liza had $800 in her checking account. On Wednesday, she paid her rent, $450. On Thursday, she deposited her $1500 paycheck. On Friday, she paid her electricity and internet bills which were $117 and $100, respectively. Then on Saturday, she paid her phone bill, $70. How much money is left in Liza's account?"""
    initial_balance = 800
    rent = 450
    deposit = 1500
    bills = 117 + 100 + 70
    final_balance = initial_balance - rent + deposit - bills
    result = final_balance
    return result

print(solution())