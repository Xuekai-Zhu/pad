def solution():
    
    starting_balance = 800
    rent = 450
    paycheck = 1500
    bills = 117 + 100 + 70
    ending_balance = starting_balance - rent + paycheck - bills
    result = ending_balance
    return result

print(solution())