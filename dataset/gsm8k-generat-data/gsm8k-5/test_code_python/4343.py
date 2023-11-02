def solution():
    daily_expenses = 30 + 12  # Janina spends $30 for rent and $12 for supplies each day
    pancake_price = 2  # Janina sells each pancake for $2

    # Calculate the number of pancakes Janina needs to sell each day
    pancakes_per_day = daily_expenses / pancake_price
    result = pancakes_per_day
    return result

print(solution())