def solution():
    """Bobby made a big batch of soup weighing 80 kg. Each day the batch gets reduced by half. How many kg will it reach on the fourth day after he made the soup?"""
    # Define the initial weight of the soup
    soup_weight = 80

    # Calculate the weight of the soup on the fourth day
    final_weight = soup_weight / 2 / 2 / 2

    # Display the weight of the soup on the fourth day
    result = final_weight
    return result

print(solution())