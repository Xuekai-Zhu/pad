def solution():
    
    watts_per_bulb = 60
    number_of_bulbs = 40
    daily_watt_usage = watts_per_bulb * number_of_bulbs
    monthly_watt_usage = daily_watt_usage * 30
    price_per_watt = 0.2
    monthly_expenses = monthly_watt_usage * price_per_watt
    result = monthly_expenses
    return result

print(solution())