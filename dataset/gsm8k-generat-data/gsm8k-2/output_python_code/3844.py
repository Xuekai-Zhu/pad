def solution():
    """During a recent three-day trip to Italy, Keziah and her mom went mushroom picking. They sold all the mushrooms they picked on the first day for a total of $58. The day after, they picked 12 mushrooms. On the last day, they picked double the mushrooms they had picked the previous day. If the price per mushroom was $2, what is the total number of mushrooms they picked?"""
    first_day_total = 58
    second_day_total = 12 * 2
    total_money = first_day_total + (second_day_total * 2)
    total_mushrooms = total_money / 2
    result = total_mushrooms
    return result

print(solution())