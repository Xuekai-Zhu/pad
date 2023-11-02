def solution():
    
    initial_balance = 230
    withdraw_amount = 60
    deposit_amount = 2 * withdraw_amount
    new_balance = initial_balance - withdraw_amount + deposit_amount
    result = new_balance
    return result

print(solution())