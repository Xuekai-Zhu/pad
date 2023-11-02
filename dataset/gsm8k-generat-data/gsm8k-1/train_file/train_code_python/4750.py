def solution():
    """Billy made 49 sandwiches; Katelyn made 47 more than that. Chloe made a quarter of the amount that Katelyn made. How many sandwiches did they make in all?"""
    billy_sandwiches = 49
    katelyn_sandwiches = billy_sandwiches + 47
    chloe_sandwiches = katelyn_sandwiches / 4
    total_sandwiches = billy_sandwiches + katelyn_sandwiches + chloe_sandwiches
    result = total_sandwiches
    return result

print(solution())