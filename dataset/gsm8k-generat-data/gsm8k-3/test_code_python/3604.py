def solution():
    """Lyanna set up a food bank to collect food to give to the homeless in her local town. In the first week, 40 pounds of food were donated to the food bank by the people of her local town. In the second week, donations were twice as high as the first week. If she gave out 70% of the donated food to the homeless in the third week, calculate the amount of food remaining in the food bank."""
    # Define the amount of food donated in the first week
    WEEK_1 = 40

    # Define the amount of food donated in the second week
    WEEK_2 = WEEK_1 * 2

    # Define the percentage of food given out in the third week
    WEEK_3_PERCENT = 0.7

    # Calculate the total amount of food donated
    total_donated = WEEK_1 + WEEK_2

    # Calculate the amount of food remaining after the third week
    remaining_food = total_donated * (1 - WEEK_3_PERCENT)

    # Display the amount of food remaining
    result = remaining_food
    return result

print(solution())