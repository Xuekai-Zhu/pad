def solution():
    first_hour_leaves = 7
    second_hour_leaves = 4
    third_hour_leaves = 4

    # Calculate the total number of leaves that fell in the first 3 hours
    total_leaves = first_hour_leaves + (second_hour_leaves * 2) + (third_hour_leaves * 3)

    # Calculate the average number of leaves that fell per hour
    avg_leaves_per_hour = total_leaves / 3
    result = avg_leaves_per_hour
    return result

print(solution())