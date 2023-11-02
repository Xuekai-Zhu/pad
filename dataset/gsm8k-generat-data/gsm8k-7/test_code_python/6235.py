def solution():
    total_distance = 140
    distance_per_liter = 70
    liters_per_distance = 10

    # Calculate the number of liters of gasoline needed for the one-way trip
    liters_needed = (total_distance / distance_per_liter) * liters_per_distance
    result = liters_needed
    return result

print(solution())