def solution():
    """Karen is paddling her canoe up a river against the current. On a still pond, Karen can paddle 10 miles per hour. The river flows in the opposite direction at 4 miles per hour. If the river is 12 miles long, how many hours will it take Karen to paddle up it?"""
    still_speed = 10
    current_speed = 4
    river_length = 12
    relative_speed = still_speed - current_speed
    time = river_length / relative_speed
    result = time
    return result

print(solution())