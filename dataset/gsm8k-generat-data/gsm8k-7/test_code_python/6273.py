def solution():
    stacy_growth = 6
    brother_growth = 1
    stacy_height_last_year = 50

    # Calculate how much taller Stacy is than her brother
    height_difference = stacy_growth - brother_growth

    # Add that height difference to Stacy's height last year to find her current height
    stacy_height_now = stacy_height_last_year + height_difference
    result = stacy_height_now
    return result

print(solution())