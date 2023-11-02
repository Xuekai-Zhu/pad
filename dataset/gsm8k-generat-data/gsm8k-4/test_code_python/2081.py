def solution():
    """Cassidy is grounded for 14 days for lying about her report card, plus 3 extra days for each grade below a B. If Cassidy got four grades below a B, how long is she grounded for?"""
    # Define the initial grounding period
    grounding_period = 14

    # Define the number of grades below a B
    grades_below_b = 4

    # Calculate the additional grounding period based on grades below a B
    additional_period = grades_below_b * 3

    # Calculate the total grounding period
    total_period = grounding_period + additional_period

    # return the result
    result = total_period
    return result

print(solution())