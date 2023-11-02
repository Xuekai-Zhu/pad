def solution():
    num_sets = 4
    num_cups_per_set = 2 * 12  # 2 dozen
    damaged_cups = 5
    unused_cups = 30

    # Calculate the total number of paper cups that Liezl prepared
    total_cups_prepared = num_sets * num_cups_per_set

    # Calculate the total number of paper cups used
    total_cups_used = total_cups_prepared - damaged_cups - unused_cups
    result = total_cups_used
    return result

print(solution())