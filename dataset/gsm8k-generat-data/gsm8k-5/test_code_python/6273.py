def solution():
    brother_growth = 1  # Stacy's brother grew 1 inch last year
    stacy_growth = brother_growth + 6  # Stacy grew 6 inches more than her brother
    height_last_year = 50  # Stacy was 50 inches tall last year

    # Calculate Stacy's current height
    current_height = height_last_year + stacy_growth
    result = current_height
    return result

print(solution())