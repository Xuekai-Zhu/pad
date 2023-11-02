def solution():
    """The first tank is 300 liters filled while the second tank is 450 liters filled. The second tank is only 45% filled. If the two tanks have the same capacity, how many more liters of water are needed to fill the two tanks?"""
    first_tank_capacity = 300
    second_tank_filled = 450
    second_tank_capacity = second_tank_filled / 0.45
    total_capacity = first_tank_capacity + second_tank_capacity
    water_needed = total_capacity - (first_tank_capacity + second_tank_filled)
    result = water_needed
    
    return result

print(solution())