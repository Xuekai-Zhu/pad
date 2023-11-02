def solution():
    """A washing machine uses 20 gallons of water for a heavy wash, 10 gallons of water for a regular wash, and 2 gallons of water for a light wash per load of laundry. If bleach is used, there is an extra light wash cycle added to rinse the laundry thoroughly. There are two heavy washes, three regular washes, and one light wash to do. Two of the loads need to be bleached. How many gallons of water will be needed?"""
    # Define the water usage per load for each type of wash
    HEAVY_WATER_USAGE = 20
    REGULAR_WATER_USAGE = 10
    LIGHT_WATER_USAGE = 2

    # Calculate the total water usage for the non-bleach loads
    total_water_usage = 2 * HEAVY_WATER_USAGE + 3 * REGULAR_WATER_USAGE + 1 * LIGHT_WATER_USAGE

    # Calculate the total water usage for the bleach loads (with an extra light wash cycle)
    total_bleach_water_usage = 2 * (LIGHT_WATER_USAGE + LIGHT_WATER_USAGE)

    # Add the total water usage for both sets of loads
    total_water_needed = total_water_usage + total_bleach_water_usage

    # return the result
    result = total_water_needed
    return result

print(solution())