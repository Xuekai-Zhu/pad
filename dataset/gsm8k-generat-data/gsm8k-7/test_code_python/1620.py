def solution():
    num_flour_bags = 3
    cups_per_pound = 2
    pounds_per_rack = 3
    current_racks = 3

    # Calculate the total amount of flour used
    total_cups_flour = num_flour_bags * 8
    total_pounds_dough = total_cups_flour / cups_per_pound

    # Calculate the total number of racks needed
    racks_needed = total_pounds_dough / pounds_per_rack
    extra_racks_needed = racks_needed - current_racks

    result = extra_racks_needed
    return result

print(solution())