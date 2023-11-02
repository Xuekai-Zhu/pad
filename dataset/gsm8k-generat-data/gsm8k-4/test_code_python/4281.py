def solution():
    """Jerry is refilling the duck pond in his backyard during a drought. The pond can hold 200 gallons of water. Jerry's hose can normally pump 6 gallons/minute, but due to drought restrictions, it can only pump 2/3rds as fast right now. How many minutes will it take Jerry to fill his pond?"""
    # Define the capacity of the pond and the normal pumping rate of the hose
    POND_CAPACITY = 200
    NORMAL_PUMPING_RATE = 6  # gallons per minute

    # Define the current pumping rate of the hose
    CURRENT_PUMPING_RATE = 2/3 * NORMAL_PUMPING_RATE  # gallons per minute

    # Calculate the time it takes to fill the pond at the current pumping rate
    time_to_fill = POND_CAPACITY / CURRENT_PUMPING_RATE  # minutes

    # return the result
    result = time_to_fill
    return result

print(solution())