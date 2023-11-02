def solution():
    """Stacy was 50 inches tall last year. If she grew 6 inches more than her brother who grew 1 inch last year, how tall is Stacy now?"""
    # Define Stacy's initial height and her brother's growth
    stacy_height = 50
    brother_growth = 1

    # Calculate Stacy's growth
    stacy_growth = brother_growth + 6

    # Calculate Stacy's current height
    stacy_current_height = stacy_height + stacy_growth

    # Return the result
    result = stacy_current_height
    return result

print(solution())