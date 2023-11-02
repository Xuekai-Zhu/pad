def solution():
    """Jerry is refilling the duck pond in his backyard during a drought. The pond can hold 200 gallons of water. Jerry's hose can normally pump 6 gallons/minute, but due to drought restrictions, it can only pump 2/3rds as fast right now. How many minutes will it take Jerry to fill his pond?"""
    # Define the pond capacity and the hose rate
    POND_CAPACITY = 200
    NORMAL_HOSE_RATE = 6
    DROUGHT_HOSE_RATE = 2/3 * NORMAL_HOSE_RATE

    # Calculate the time it takes to fill the pond with the normal hose rate
    normal_time = POND_CAPACITY / NORMAL_HOSE_RATE

    # Calculate the time it takes to fill the pond with the drought hose rate
    drought_time = POND_CAPACITY / DROUGHT_HOSE_RATE

    # Display the time it takes to fill the pond
    result = drought_time
    return result

print(solution())