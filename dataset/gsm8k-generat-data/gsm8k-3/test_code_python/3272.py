def solution():
    """John has a very inefficient toilet that uses 5 gallons of water per flush and his household flushed 15 times per day.  He replaced it with a toilet that uses 80% less water per flush.  How much water did John save in June?"""
    # Define the amount of water used per flush (in gallons)
    OLD_TOILET_WATER_USAGE = 5
    NEW_TOILET_WATER_USAGE = OLD_TOILET_WATER_USAGE * 0.2  # 80% less water usage

    # Define the number of flushes per day
    FLUSHES_PER_DAY = 15

    # Calculate the amount of water saved per flush
    WATER_SAVED_PER_FLUSH = OLD_TOILET_WATER_USAGE - NEW_TOILET_WATER_USAGE

    # Calculate the amount of water saved per day
    WATER_SAVED_PER_DAY = WATER_SAVED_PER_FLUSH * FLUSHES_PER_DAY

    # Calculate the amount of water saved in June (assuming 30 days in June)
    WATER_SAVED_IN_JUNE = WATER_SAVED_PER_DAY * 30

    # Display the amount of water saved in June
    result = WATER_SAVED_IN_JUNE
    return result

print(solution())