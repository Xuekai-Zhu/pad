def solution():
    
    hours = 8
    hourly_rate = 18
    total_earning = hours * hourly_rate
    money_spent = total_earning / 2
    remaining_money = total_earning - money_spent
    result = remaining_money
    return result

print(solution())