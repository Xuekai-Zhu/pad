def solution():
    """Karen is paddling her canoe up a river against the current. On a still pond, Karen can paddle 10 miles per hour. The river flows in the opposite direction at 4 miles per hour. If the river is 12 miles long, how many hours will it take Karen to paddle up it?"""
    # Define Karen's paddling speed and the speed of the river
    KAREN_SPEED = 10
    RIVER_SPEED = 4

    # Define the distance to be paddled
    DISTANCE = 12

    # Calculate Karen's effective paddling speed against the current
    effective_speed = KAREN_SPEED - RIVER_SPEED

    # Calculate the time it will take Karen to paddle up the river
    time = DISTANCE / effective_speed

    result = time
    return result

print(solution())