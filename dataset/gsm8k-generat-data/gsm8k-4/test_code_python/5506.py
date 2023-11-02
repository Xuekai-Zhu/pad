def solution():
    """The first tank is 300 liters filled while the second tank is 450 liters filled. The second tank is only 45% filled. If the two tanks have the same capacity, how many more liters of water are needed to fill the two tanks?"""
    # Calculate the total capacity of the two tanks
    total_capacity = 300 + (450 / 0.45)

    # Calculate the current total amount of water in the two tanks
    current_total_water = 300 + 450

    # Calculate the amount of water needed to fill the two tanks
    water_needed = total_capacity - current_total_water

    # return the result
    result = water_needed
    return result

print(solution())