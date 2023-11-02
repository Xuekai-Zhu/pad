def solution():
    """Stacy was 50 inches tall last year. If she grew 6 inches more than her brother who grew 1 inch last year, how tall is Stacy now?"""
    # Define Stacy's growth rate and her brother's growth rate
    STACY_RATE = 1
    BROTHER_RATE = 1

    # Define Stacy's initial height and her brother's initial height
    stacy_height = 50
    brother_height = 0

    # Calculate Stacy's current height
    stacy_height += STACY_RATE * (brother_height + 6)

    # Display Stacy's current height
    result = stacy_height
    return result

print(solution())