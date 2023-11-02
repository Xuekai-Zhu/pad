def solution():
    num_squirrels = 5
    total_num_acorns = 575
    acorns_per_squirrel = 130

    # Calculate the total number of acorns needed by all squirrels
    total_acorns_needed = num_squirrels * acorns_per_squirrel

    # Calculate the number of acorns still needed by all squirrels
    total_acorns_left = total_acorns_needed - total_num_acorns

    # Calculate the number of acorns each squirrel still needs to collect
    acorns_needed_per_squirrel = total_acorns_left / num_squirrels
    result = acorns_needed_per_squirrel
    return result

print(solution())