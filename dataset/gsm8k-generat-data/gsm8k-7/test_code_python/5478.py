def solution():
    tank_capacity = 100
    initial_fill = 2/5 * tank_capacity
    collected_first_day = 15
    collected_second_day = collected_first_day + 5
    
    # Calculate the total amount of water in the tank after the first two days
    total_water = initial_fill + collected_first_day + collected_second_day
    
    # Calculate the amount of water collected on the third day
    collected_third_day = tank_capacity - total_water
    
    result = collected_third_day
    return result

print(solution())