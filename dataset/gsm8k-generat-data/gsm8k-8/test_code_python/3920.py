def solution():
    # Define initial alligator count and growth rate
    initial_count = 4
    growth_rate = 2

    # Calculate the number of alligators after 6 months
    after_6_months = initial_count * growth_rate

    # Calculate the number of alligators after 12 months
    after_12_months = after_6_months * growth_rate

    result = after_12_months
    return result

print(solution())