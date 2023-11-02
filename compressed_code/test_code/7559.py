def solution():
    
    hours_per_day = 3
    rate_per_hour = 10
    money_earned = hours_per_day * rate_per_hour * 7 
    makeup_spending = money_earned * (3/10)
    skincare_spending = money_earned * (2/5)
    remaining_money = money_earned - makeup_spending - skincare_spending
    result = remaining_money
    return result

print(solution())