def solution():
    """Jane is painting her fingernails. She applies a base coat that takes 2 minutes to dry,
    two color coats that take 3 minutes each to dry, and a clear top coat that takes 5 minutes to dry.
    How many minutes total does Jane spend waiting for her nail polish to dry?"""
    # Define the drying times for each coat
    BASE_COAT_DRY_TIME = 2
    COLOR_COAT_DRY_TIME = 3
    TOP_COAT_DRY_TIME = 5

    # Calculate the total drying time
    total_dry_time = BASE_COAT_DRY_TIME + (2 * COLOR_COAT_DRY_TIME) + TOP_COAT_DRY_TIME

    # Display the total drying time
    result = total_dry_time
    return result

print(solution())