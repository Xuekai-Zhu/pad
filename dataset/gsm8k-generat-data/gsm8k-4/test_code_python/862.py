def solution():
    """5 squirrels collected 575 acorns. If each squirrel needs 130 acorns to get through the winter, how many more acorns does each squirrel need to collect?"""
    # Define the number of squirrels and the total number of acorns collected
    num_squirrels = 5
    total_acorns = 575

    # Define the number of acorns needed per squirrel to get through the winter
    acorns_per_squirrel = 130

    # Calculate the total number of acorns needed by all squirrels
    total_acorns_needed = num_squirrels * acorns_per_squirrel

    # Calculate the number of additional acorns needed by each squirrel
    extra_acorns_needed = total_acorns_needed - total_acorns
    acorns_per_squirrel_needed = extra_acorns_needed / num_squirrels

    # Return the result
    result = acorns_per_squirrel_needed
    return result

print(solution())