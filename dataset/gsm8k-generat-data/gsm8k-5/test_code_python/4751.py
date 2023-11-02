def solution():
    billy_sandwiches = 49  # Billy made 49 sandwiches
    katelyn_sandwiches = billy_sandwiches + 47  # Katelyn made 47 more sandwiches than Billy
    chloe_sandwiches = katelyn_sandwiches / 4  # Chloe made 1/4 of the amount that Katelyn made

    # Calculate the total number of sandwiches made by all of them
    total_sandwiches = billy_sandwiches + katelyn_sandwiches + chloe_sandwiches
    result = total_sandwiches
    return result

print(solution())