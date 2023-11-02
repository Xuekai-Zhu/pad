def solution():
    """John is a door-to-door salesman. He visits 50 houses a day. 20% of them buy something from them. Of those that buy something half buy a $50 set of knives and the other half buy a $150 set of knives. How much does he sell a week when he works 5 days a week?"""
    houses_per_day = 50
    days_per_week = 5
    buy_percentage = 0.2
    half_buy_50 = 0.5
    half_buy_150 = 0.5
    price_50 = 50
    price_150 = 150
    
    # Calculate the number of houses that buy something from him each day
    houses_buying = houses_per_day * buy_percentage
    
    # Calculate the number of houses that buys a $50 set and a $150 set each day
    houses_buying_50 = houses_buying * half_buy_50
    houses_buying_150 = houses_buying * half_buy_150
    
    # Calculate the total amount of money he makes each day and each week
    money_50 = houses_buying_50 * price_50
    money_150 = houses_buying_150 * price_150
    daily_income = money_50 + money_150
    weekly_income = daily_income * days_per_week
    
    result = weekly_income
    return result

print(solution())