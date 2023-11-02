def solution():
    # Calculate the total number of acorns collected
    total_acorns = 575

    # Calculate the number of acorns each squirrel needs to get through the winter
    acorns_per_squirrel = 130

    # Calculate the total number of acorns needed by all the squirrels
    total_acorns_needed = acorns_per_squirrel * 5

    # Calculate the remaining number of acorns needed by each squirrel
    remaining_acorns_per_squirrel = total_acorns_needed - total_acorns / 5

    result = remaining_acorns_per_squirrel
    return result

print(solution())