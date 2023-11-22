def solution():
    
    # Define the maximum load and weight of an adult
    MAX_LOAD = 700
    ADULT_WEIGHT = 80

    # Calculate the total weight of the adults
    total_adult_weight = ADULT_WEIGHT * 8

    # Calculate the total weight of the elevator
    total_elevation_weight = total_adult_weight * 8

    # Calculate the excess weight exceeded the maximum load
    excess_weight = MAX_LOAD - total_elevation_weight

    # Display the excess weight exceeded
    result = excess_weight
    return result

print(solution())