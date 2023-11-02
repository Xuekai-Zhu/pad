def solution():
    # Calculate the total toothpaste used in one day by the family
    total_toothpaste_used_per_day = (3 + 2 + 1 + 1) * 3

    # Calculate the number of days the toothpaste will last
    num_days_toothpaste_will_last = 105 / total_toothpaste_used_per_day

    # Round up to the nearest integer
    num_days_toothpaste_will_last = math.ceil(num_days_toothpaste_will_last)

    result = num_days_toothpaste_will_last
    return result

print(solution())