def solution():
    """John takes a 10-minute shower every other day for 4 weeks. If his shower uses 2 gallons of water per minute. How much water does he use in those 4 weeks?"""
    # Define the number of weeks and days John takes a shower
    NUM_WEEKS = 4
    NUM_SHOWER_DAYS = 7  # every other day

    # Define the shower duration and water usage rate
    SHOWER_DURATION = 10  # minutes
    WATER_USAGE_RATE = 2  # gallons per minute

    # Calculate the total number of showers John takes in 4 weeks
    num_showers = NUM_WEEKS * (NUM_SHOWER_DAYS // 2)

    # Calculate the total water usage
    water_usage = num_showers * SHOWER_DURATION * WATER_USAGE_RATE

    # Display the total water usage
    result = water_usage
    return result

print(solution())