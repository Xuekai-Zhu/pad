def solution():
    
    starting_amount = 100
    daily_spending = 8
    remaining_amount = starting_amount - (daily_spending * 7)
    bills = remaining_amount // 5
    remaining_balance = remaining_amount - (bills * 5)
    result = remaining_balance
    return result

print(solution())