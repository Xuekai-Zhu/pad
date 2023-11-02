def solution():
    """Bella eats 6 apples a day. If during the week she consumes a third of the apples Grace picks, how many apples will Grace have after 6 weeks?"""
    # Define the number of apples Bella eats per day
    BELLA_APPLES = 6

    # Define the fraction of Grace's apples that Bella consumes each week
    BELLA_FRACTION = 1/3

    # Define the number of weeks
    WEEKS = 6

    # Calculate the total number of apples Grace picked in 6 weeks
    grace_apples = (7 - 1) * BELLA_APPLES * (1 - BELLA_FRACTION) * WEEKS

    # Display the total number of apples Grace has after 6 weeks
    result = grace_apples
    return result

print(solution())