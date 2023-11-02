def solution():
    # Define starting distance and total increase
    starting_distance = 3
    total_increase = 4

    # Calculate final distance
    final_distance = starting_distance + total_increase * (1 + 2 + 3 + 4)

    # Calculate average distance per day
    average_distance_per_day = final_distance / 35

    # Round to nearest tenth
    result = round(average_distance_per_day, 1)
    return result

print(solution())