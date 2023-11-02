def solution():
    # Define the capacity of the water tank and the rate of filling
    capacity = 4000
    filling_rate = 10

    # Calculate the amount of water needed to fill the tank to 3/4 of its capacity
    three_fourths = 0.75
    water_needed = capacity * three_fourths

    # Calculate the time it will take to fill the tank to the desired amount
    time_needed = water_needed / filling_rate
    result = time_needed
    return result

print(solution())