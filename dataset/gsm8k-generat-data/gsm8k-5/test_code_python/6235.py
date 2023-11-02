def solution():
    distance_one_way = 140  # Samson is going to a town that is 140 km away
    distance_per_liter = 70  # Samson's car travels 70 km per 10 liters of gasoline

    # Calculate the total liters of gasoline Samson needs for a one-way trip
    total_liters = distance_one_way / distance_per_liter * 10
    result = total_liters
    return result

print(solution())