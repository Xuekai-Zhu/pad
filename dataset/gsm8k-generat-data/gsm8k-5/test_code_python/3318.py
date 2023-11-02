def solution():
    # Last night's dinner
    apples_last_night = 3
    bananas_last_night = 1
    oranges_last_night = 4

    # Today's planned dinner
    apples_today = apples_last_night + 4
    bananas_today = bananas_last_night * 10
    oranges_today = apples_today * 2

    # Total number of fruits eaten so far
    total_fruits = apples_last_night + bananas_last_night + oranges_last_night + apples_today + bananas_today + oranges_today
    result = total_fruits
    return result

print(solution())