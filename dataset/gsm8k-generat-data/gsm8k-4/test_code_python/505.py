def solution():
    """Carla's sheepdog rounded up 90% of her sheep, but the remaining 10% wandered off into the hills. If there are 81 sheep in the pen, how many are out in the wilderness?"""
    # Define the percentage of sheep rounded up by the sheepdog
    rounded_up_percentage = 0.9

    # Define the number of sheep in the pen
    sheep_in_pen = 81

    # Calculate the total number of sheep
    total_sheep = sheep_in_pen / rounded_up_percentage

    # Calculate the number of sheep in the wilderness
    wilderness_sheep = total_sheep - sheep_in_pen

    # return the result
    result = wilderness_sheep
    return result

print(solution())