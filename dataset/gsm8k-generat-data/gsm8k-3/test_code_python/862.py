def solution():
    """5 squirrels collected 575 acorns. If each squirrel needs 130 acorns to get through the winter, how many more acorns does each squirrel need to collect?"""
    # Define the number of squirrels and the number of collected acorns
    NUM_SQUIRRELS = 5
    COLLECTED_ACORNS = 575

    # Define the number of acorns needed by each squirrel for the winter
    ACORNS_PER_SQUIRREL = 130

    # Calculate the total number of acorns needed by all squirrels for the winter
    total_acorns_needed = NUM_SQUIRRELS * ACORNS_PER_SQUIRREL

    # Calculate the remaining acorns needed to get through the winter for each squirrel
    remaining_acorns_per_squirrel = total_acorns_needed - COLLECTED_ACORNS
    additional_acorns_per_squirrel = remaining_acorns_per_squirrel / NUM_SQUIRRELS

    # Display the additional acorns needed per squirrel
    result = additional_acorns_per_squirrel
    return result

print(solution())