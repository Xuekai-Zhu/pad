def solution():
    morning_1 = 68
    evening_1 = 82
    morning_2 = morning_1 - 18
    total_milk = morning_1 + evening_1 + morning_2
    sold = total_milk - 24
    price_per_gallon = 3.5
    revenue = sold * price_per_gallon
    result = revenue
    return result

print(solution())