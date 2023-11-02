def solution():
    
    dress_price = 80
    savings = 20
    weekly_allowance = 30
    weekly_spending = 10
    remaining_price = dress_price - savings
    weeks_to_save = 0
    while remaining_price > 0:
        weeks_to_save += 1
        remaining_price -= (weekly_allowance - weekly_spending)
    result = weeks_to_save
    return result

print(solution())