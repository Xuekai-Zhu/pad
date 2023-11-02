def solution():
    """Jack leaves his bathtub's faucet dripping at a rate of 40 ml/minute. Water evaporates from the bathtub at a rate of 200 ml/hour. If he leaves the water running for 9 hours, then dumps out 12 liters, how many milliliters of water are left in the bathtub?"""
    # Define the initial volume of water in the bathtub in milliliters
    initial_volume = 0

    # Calculate the total amount of water added to the bathtub from the dripping faucet
    faucet_rate = 40 # milliliters per minute
    total_faucet_volume = faucet_rate * 60 * 9 # milliliters

    # Calculate the total amount of water that has evaporated from the bathtub
    evaporation_rate = 200 # milliliters per hour
    total_evaporation_volume = evaporation_rate * 9 # milliliters

    # Calculate the total amount of water that has been dumped out
    dumped_volume = 12000 # milliliters

    # Calculate the remaining volume of water in the bathtub
    remaining_volume = initial_volume + total_faucet_volume - total_evaporation_volume - dumped_volume

    result = remaining_volume
    return result

print(solution())