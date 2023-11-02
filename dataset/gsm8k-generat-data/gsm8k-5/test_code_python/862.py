def solution():
    total_acorns = 575  # The total number of acorns collected by 5 squirrels
    num_squirrels = 5  # There are 5 squirrels
    acorns_per_squirrel_needed = 130  # Each squirrel needs 130 acorns to get through the winter

    # Calculate the total number of acorns needed by all squirrels
    total_acorns_needed = num_squirrels * acorns_per_squirrel_needed

    # Calculate the number of additional acorns each squirrel needs to collect
    additional_acorns_needed = total_acorns_needed - total_acorns
    acorns_per_squirrel = additional_acorns_needed / num_squirrels
    result = acorns_per_squirrel
    return result

print(solution())