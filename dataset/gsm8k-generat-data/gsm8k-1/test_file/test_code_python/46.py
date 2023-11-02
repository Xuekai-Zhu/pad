def solution():
    """Lloyd has an egg farm. His chickens produce 252 eggs per day and he sells them for $2 per dozen. How much does Lloyd make on eggs per week?"""
    eggs_per_day = 252
    dozens_per_day = eggs_per_day / 12
    price_per_dozen = 2
    income_per_day = dozens_per_day * price_per_dozen
    income_per_week = income_per_day * 7
    result = income_per_week
    return result

print(solution())