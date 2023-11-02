def solution():
    """Last night Kannon had 3 apples, a banana, and 4 oranges for dinner. Today she is planning to have 4 more apples than last night, 10 times as many bananas as she ate last night, and twice as many oranges as apples she'll have today. How many fruits would she have eaten so far in the two meals?"""
    last_night_apples = 3
    last_night_bananas = 1
    last_night_oranges = 4
    today_apples = last_night_apples + 4
    today_bananas = last_night_bananas * 10
    today_oranges = today_apples * 2
    total_fruits = last_night_apples + last_night_bananas + last_night_oranges + today_apples + today_bananas + today_oranges
    result = total_fruits
    return result

print(solution())