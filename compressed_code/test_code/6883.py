def solution():
    
    morning_yesterday = 68
    evening_yesterday = 82
    morning_today = morning_yesterday - 18
    total_milk = morning_yesterday + evening_yesterday + morning_today
    sold_milk = total_milk - 24
    price_per_gallon = 3.50
    revenue = sold_milk * price_per_gallon
    result = revenue
    return result

print(solution())