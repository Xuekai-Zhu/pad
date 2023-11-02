def solution():
    """Annie is building a diorama for her history class. The amount of time she spent building it is equal to three times the amount of time she spent planning it minus 5 minutes. If she spent 67 minutes on the diorama total, how many minutes did she spend building it?"""
    
    # Let's assume the time Annie spent planning is x in minutes
    # Then the time Annie spent building is 3x - 5
    # And we know the total time is 67 minutes
    # So we can set up the equation: x + 3x - 5 = 67
    
    # Simplifying the equation, we get:
    # 4x - 5 = 67
    # 4x = 72
    # x = 18
    
    # So Annie spent 18 minutes planning and 3(18) - 5 = 49 minutes building
    result = 49
    return result

print(solution())