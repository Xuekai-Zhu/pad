def solution():
    """Jack leaves his bathtub's faucet dripping at a rate of 40 ml/minute. Water evaporates from the bathtub at a rate of 200 ml/hour. If he leaves the water running for 9 hours, then dumps out 12 liters, how many milliliters of water are left in the bathtub?"""
    # Define the drip rate and evaporation rate
    DRIP_RATE = 40 / 60  # ml/minute to ml/second
    EVAPORATION_RATE = 200 / 60 / 60  # ml/hour to ml/second

    # Calculate the total amount of water added during the 9 hours
    total_added = DRIP_RATE * 60 * 60 * 9  # ml/second * seconds = ml

    # Calculate the amount of water that evaporated during the 9 hours
    total_evaporated = EVAPORATION_RATE * 60 * 60 * 9  # ml/second * seconds = ml

    # Calculate the total amount of water left in the bathtub
    total_left = total_added - total_evaporated - 12000  # ml - ml - ml = ml

    # Display the total amount of water left
    result = total_left
    return result

print(solution())