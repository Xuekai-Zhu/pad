def solution():
    
    hours_worked = 8
    wage_per_hour = 18
    money_made = hours_worked * wage_per_hour
    money_spent = money_made / 2
    money_left = money_made - money_spent
    result = money_left
    return result

print(solution())