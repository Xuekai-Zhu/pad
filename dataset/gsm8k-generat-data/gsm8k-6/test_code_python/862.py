def solution():
    # Calculate the total number of acorns needed by the squirrels
    total_acorns_needed = 5 * 130

    # Calculate the remaining number of acorns needed by each squirrel
    remaining_acorns_needed = total_acorns_needed - 575
    acorns_per_squirrel = remaining_acorns_needed / 5  # Divide by number of squirrels
    result = acorns_per_squirrel
    return result

print(solution())