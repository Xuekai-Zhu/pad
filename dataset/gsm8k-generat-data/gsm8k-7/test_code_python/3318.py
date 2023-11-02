def solution():
    apples_last_night = 3
    bananas_last_night = 1  # 1 banana
    oranges_last_night = 4

    apples_today = apples_last_night + 4  # 4 more apples
    bananas_today = bananas_last_night * 10  # 10 times as many bananas
    oranges_today = apples_today * 2  # Twice as many oranges as apples today

    # Calculate the total number of fruits eaten in both meals
    total_fruits = apples_last_night + bananas_last_night + oranges_last_night + apples_today + bananas_today + oranges_today
    result = total_fruits
    return result

print(solution())