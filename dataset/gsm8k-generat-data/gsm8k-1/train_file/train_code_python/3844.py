def solution():
    """During a recent three-day trip to Italy, Keziah and her mom went mushroom picking. They sold all the mushrooms they picked on the first day for a total of $58. The day after, they picked 12 mushrooms. On the last day, they picked double the mushrooms they had picked the previous day. If the price per mushroom was $2, what is the total number of mushrooms they picked?"""
    price_per_mushroom = 2
    mushrooms_first_day = 58 // price_per_mushroom
    mushrooms_second_day = 12
    mushrooms_third_day = mushrooms_second_day * 2
    total_mushrooms = mushrooms_first_day + mushrooms_second_day + mushrooms_third_day
    result = total_mushrooms
    return result

print(solution())