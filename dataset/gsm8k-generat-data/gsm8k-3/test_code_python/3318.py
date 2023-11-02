def solution():
    """Last night Kannon had 3 apples, a banana, and 4 oranges for dinner. Today she is planning to have 4 more apples than last night, 10 times as many bananas as she ate last night, and twice as many oranges as apples she'll have today. How many fruits would she have eaten so far in the two meals?"""
    # Define the number of fruits Kannon had last night
    apples_last_night = 3
    banana_last_night = 1
    oranges_last_night = 4

    # Define the number of fruits Kannon is planning to have today
    apples_today = apples_last_night + 4
    banana_today = banana_last_night * 10
    oranges_today = apples_today * 2

    # Calculate the total number of fruits Kannon will have eaten
    total_apples = apples_last_night + apples_today
    total_bananas = banana_last_night + banana_today
    total_oranges = oranges_last_night + oranges_today
    total_fruits = total_apples + total_bananas + total_oranges

    # Display the total number of fruits eaten
    result = total_fruits
    return result

print(solution())