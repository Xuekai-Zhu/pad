def solution():
    """During a recent three-day trip to Italy, Keziah and her mom went mushroom picking. They sold all the mushrooms they picked on the first day for a total of $58. The day after, they picked 12 mushrooms. On the last day, they picked double the mushrooms they had picked the previous day. If the price per mushroom was $2, what is the total number of mushrooms they picked?"""
    # Define the variables
    mushrooms_1 = None
    mushrooms_2 = 12
    mushrooms_3 = None

    # Calculate the total mushrooms picked on the first day
    total_mushrooms = 58 / 2

    # Calculate the total mushrooms picked on the last day
    mushrooms_3 = mushrooms_2 * 2

    # Calculate the total number of mushrooms picked
    mushrooms_total = total_mushrooms + mushrooms_2 + mushrooms_3

    # return the result
    result = mushrooms_total
    return result

print(solution())