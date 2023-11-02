def solution():
    """Carla's sheepdog rounded up 90% of her sheep, but the remaining 10% wandered off into the hills. If there are 81 sheep in the pen, how many are out in the wilderness?"""
    # Define the percentage of sheep rounded up and lost
    ROUNDED_UP_PERCENTAGE = 0.9
    LOST_PERCENTAGE = 0.1

    # Calculate the number of sheep rounded up
    rounded_up_sheep = round(ROUNDED_UP_PERCENTAGE * 81)

    # Calculate the number of lost sheep
    lost_sheep = round(LOST_PERCENTAGE * 81)

    # Calculate the number of sheep in the wilderness
    wilderness_sheep = lost_sheep

    # Display the number of sheep in the wilderness
    result = wilderness_sheep
    return result

print(solution())