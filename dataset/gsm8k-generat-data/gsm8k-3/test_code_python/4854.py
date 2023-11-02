def solution():
    """In Zeoland the fine for speeding is $16 for each mile per hour the driver is traveling over the posted speed limit. In Zeoland, Jed was fined $256 for speeding on a road with a posted speed limit of 50 mph. Jed was fined for traveling at what speed in miles per hour?"""
    # Define the posted speed limit
    POSTED_LIMIT = 50

    # Define the fine per mile per hour over the limit
    FINE_PER_MPH = 16

    # Calculate the amount Jed was over the limit
    amount_over = 256 / FINE_PER_MPH

    # Calculate Jed's speed in miles per hour
    speed = POSTED_LIMIT + amount_over

    # Display Jed's speed
    result = speed
    return result

print(solution())