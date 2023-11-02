def solution():
    """Janina spends $30 each day for rent and uses $12 worth of supplies daily to run her pancake stand. If she sells each pancake for $2, how many pancakes must Janina sell each day to cover her expenses?"""
    expenses_per_day = 30 + 12
    pancake_price = 2
    pancakes_needed_per_day = expenses_per_day / pancake_price
    result = pancakes_needed_per_day
    return result

print(solution())