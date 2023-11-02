def solution():
    """Janina spends $30 each day for rent and uses $12 worth of supplies daily to run her pancake stand. If she sells each pancake for $2, how many pancakes must Janina sell each day to cover her expenses?"""
    expenses_per_day = 30 + 12
    price_per_pancake = 2
    pancakes_to_sell = expenses_per_day / price_per_pancake
    result = pancakes_to_sell
    return result

print(solution())