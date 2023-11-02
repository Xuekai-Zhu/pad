def solution():
    """The first tank is 300 liters filled while the second tank is 450 liters filled. The second tank is only 45% filled. If the two tanks have the same capacity, how many more liters of water are needed to fill the two tanks?"""
    second_tank_capacity = 450 / 0.45
    total_capacity = 2 * second_tank_capacity
    water_needed = total_capacity - 300 - 450
    result = water_needed
    return result

print(solution())