def solution():
    troy_distance = 75    # meters
    emily_distance = 98   # meters
    num_days = 5

    # Calculate the total distance walked by Troy in five days
    troy_total_distance = 2 * troy_distance * num_days

    # Calculate the total distance walked by Emily in five days
    emily_total_distance = 2 * emily_distance * num_days

    # Calculate the difference in distance between Emily and Troy
    difference = emily_total_distance - troy_total_distance
    result = difference
    return result

print(solution())