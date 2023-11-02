def solution():
    """Bobby made a big batch of soup weighing 80 kg. Each day the batch gets reduced by half. How many kg will it reach on the fourth day after he made the soup?"""
    # Define the initial weight of the soup
    soup_weight = 80

    # Calculate the weight of the soup after 4 days (halving each day)
    soup_weight_after_1_day = soup_weight / 2
    soup_weight_after_2_days = soup_weight_after_1_day / 2
    soup_weight_after_3_days = soup_weight_after_2_days / 2
    soup_weight_after_4_days = soup_weight_after_3_days / 2

    # Display the weight of the soup after 4 days
    result = soup_weight_after_4_days
    return result

print(solution())