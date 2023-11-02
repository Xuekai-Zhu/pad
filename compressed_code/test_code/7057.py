def solution():
    
    houses_per_day = 50
    days_per_week = 5
    buy_percentage = 0.2
    half_buy_50 = 0.5
    half_buy_150 = 0.5
    price_50 = 50
    price_150 = 150
    
    
    houses_buying = houses_per_day * buy_percentage
    
    
    houses_buying_50 = houses_buying * half_buy_50
    houses_buying_150 = houses_buying * half_buy_150
    
    
    money_50 = houses_buying_50 * price_50
    money_150 = houses_buying_150 * price_150
    daily_income = money_50 + money_150
    weekly_income = daily_income * days_per_week
    
    result = weekly_income
    return result

print(solution())