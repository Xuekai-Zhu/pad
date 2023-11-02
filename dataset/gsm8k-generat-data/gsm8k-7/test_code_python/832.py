def solution():
    num_balloons = 1000
    balloon_capacity = 10 # liters
    tank_capacity = 500 # liters

    # Calculate the total volume of air needed to fill all the balloons
    total_air_volume = num_balloons * balloon_capacity

    # Calculate the total number of tanks needed
    num_tanks = total_air_volume / tank_capacity

    # Round up to the nearest integer
    num_tanks = math.ceil(num_tanks)

    result = num_tanks
    return result

print(solution())