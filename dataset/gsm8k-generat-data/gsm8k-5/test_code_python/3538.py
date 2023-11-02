def solution():
    total_distance = 135 + 124 + 159 + 189  # Carrie drove a total of 607 miles in four days
    charging_distance = 106  # Carrie needs to charge her phone every 106 miles

    # Calculate the number of times she charged her phone
    charging_times = total_distance // charging_distance
    result = charging_times
    return result

print(solution())