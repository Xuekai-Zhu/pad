def solution():
    """Gabriel wants to buy a car for $10000 and a phone for $800. Gabriel has $5000 from working on weekends and his brother gave him $200 to help him. How much money does he still need?"""
    car_cost = 10000
    phone_cost = 800
    money_available = 5000 + 200
    money_needed = car_cost + phone_cost - money_available
    result = money_needed
    return result

print(solution())