def solution():
    # Calculate the amount of water used by the city for industrial purposes
    industrial_water = 0.8 * 40

    # Calculate the amount of water used by the city for non-industrial purposes
    non_industrial_water = 0.8 * industrial_water

    # Calculate the percentage of the total water used by the city for non-industrial purposes
    non_industrial_percentage = non_industrial_water / total_water * 100
    result = non_industrial_percentage
    return result

print(solution())