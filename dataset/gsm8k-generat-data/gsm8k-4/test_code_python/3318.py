def solution():
    """Last night Kannon had 3 apples, a banana, and 4 oranges for dinner. Today she is planning to have 4 more apples than last night, 10 times as many bananas as she ate last night, and twice as many oranges as apples she'll have today. How many fruits would she have eaten so far in the two meals?"""
    # Define the number of fruits eaten last night
    apples_last_night = 3
    banana_last_night = 1
    oranges_last_night = 4

    # Calculate the planned number of fruits for today's meal
    apples_today = apples_last_night + 4
    bananas_today = banana_last_night * 10
    oranges_today = apples_today * 2

    # Calculate the total number of fruits eaten so far
    total_apples = apples_last_night + apples_today
    total_bananas = banana_last_night + bananas_today
    total_oranges = oranges_last_night + oranges_today

    # Calculate the overall total of fruits eaten
    total_fruits = total_apples + total_bananas + total_oranges

    # return the result
    result = total_fruits
    return result

print(solution())