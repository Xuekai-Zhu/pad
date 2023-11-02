def solution():
    
    initial_balance = 800
    rent = 450
    deposit = 1500
    bills = 117 + 100 + 70
    final_balance = initial_balance - rent + deposit - bills
    result = final_balance
    return result

print(solution())