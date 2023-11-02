def solution():
    """Jerry is refilling the duck pond in his backyard during a drought. The pond can hold 200 gallons of water. Jerry's hose can normally pump 6 gallons/minute, but due to drought restrictions, it can only pump 2/3rds as fast right now. How many minutes will it take Jerry to fill his pond?"""
    pond_capacity = 200
    normal_pump_rate = 6  # gallons/minute
    drought_pump_rate = 2/3 * normal_pump_rate
    time_to_fill = pond_capacity / drought_pump_rate
    result = time_to_fill
    return result

print(solution())