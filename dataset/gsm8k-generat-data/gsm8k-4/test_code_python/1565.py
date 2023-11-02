def solution():
    """Jane is painting her fingernails. She applies a base coat that takes 2 minutes to dry, two color coats that take 3 minutes each to dry, and a clear top coat that takes 5 minutes to dry. How many minutes total does Jane spend waiting for her nail polish to dry?"""
    # Define the drying times for each coat
    base_coat_time = 2
    color_coat_time = 3
    top_coat_time = 5

    # Calculate the total drying time for all coats
    total_drying_time = base_coat_time + (2 * color_coat_time) + top_coat_time

    # Return the result
    result = total_drying_time
    return result

print(solution())