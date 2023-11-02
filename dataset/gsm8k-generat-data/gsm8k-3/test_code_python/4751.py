def solution():
    """Billy made 49 sandwiches; Katelyn made 47 more than that. Chloe made a quarter of the amount that Katelyn made. How many sandwiches did they make in all?"""
    # Define the number of sandwiches Billy made
    billy_sandwiches = 49

    # Calculate the number of sandwiches Katelyn made
    katelyn_sandwiches = billy_sandwiches + 47

    # Calculate the number of sandwiches Chloe made
    chloe_sandwiches = katelyn_sandwiches / 4

    # Calculate the total number of sandwiches made
    total_sandwiches = billy_sandwiches + katelyn_sandwiches + chloe_sandwiches

    # Display the total number of sandwiches made
    result = total_sandwiches
    return result

print(solution())