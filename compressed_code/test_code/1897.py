def solution():
    
    starting_balance = 100
    weekly_expenses = 7 * 8
    remaining_balance = starting_balance - weekly_expenses
    num_fives = remaining_balance // 5
    remaining_balance -= num_fives * 5
    result = remaining_balance
    return result

print(solution())