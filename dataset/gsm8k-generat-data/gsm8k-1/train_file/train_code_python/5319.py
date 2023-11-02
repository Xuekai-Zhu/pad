def solution():
    """Jack leaves his bathtub's faucet dripping at a rate of 40 ml/minute. Water evaporates from the bathtub at a rate of 200 ml/hour.
     If he leaves the water running for 9 hours, then dumps out 12 liters, how many milliliters of water are left in the bathtub?"""
    faucet_rate = 40
    evaporation_rate = 200
    total_minutes = 9 * 60
    total_water_added = faucet_rate * total_minutes
    total_water_evaporated = (evaporation_rate / 60) * 9
    total_water_removed = 12000
    remaining_water = total_water_added - total_water_evaporated - total_water_removed
    result = remaining_water
    return result

print(solution())