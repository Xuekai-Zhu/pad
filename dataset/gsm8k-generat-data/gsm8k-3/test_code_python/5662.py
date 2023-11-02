def solution():
    """Karen is paddling her canoe up a river against the current. On a still pond, Karen can paddle 10 miles per hour. The river flows in the opposite direction at 4 miles per hour. If the river is 12 miles long, how many hours will it take Karen to paddle up it?"""
    # Define Karen's paddling speed and the speed of the river
    KAREN_SPEED = 10
    RIVER_SPEED = 4

    # Define the length of the river
    RIVER_LENGTH = 12

    # Calculate Karen's paddling speed against the current
    karen_paddle_speed = KAREN_SPEED - RIVER_SPEED

    # Calculate the time it takes Karen to paddle up the river
    time = RIVER_LENGTH / karen_paddle_speed

    # Display the time it takes Karen to paddle up the river
    result = time
    return result

print(solution())