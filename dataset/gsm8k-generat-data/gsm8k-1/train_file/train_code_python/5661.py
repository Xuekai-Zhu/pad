def solution():
    """Karen is paddling her canoe up a river against the current. On a still pond, Karen can paddle 10 miles per hour. The river flows in the opposite direction at 4 miles per hour. If the river is 12 miles long, how many hours will it take Karen to paddle up it?"""
    speed_on_still_pond = 10
    speed_of_current = 4
    distance_to_travel = 12
    
    # Karen's speed against the current is reduced by the speed of the current.
    speed_vs_current = speed_on_still_pond - speed_of_current
    
    # We can calculate the time it takes her to travel the 12 mile distance using the formula: time = distance / speed.
    time_in_hours = distance_to_travel / speed_vs_current
    
    result = time_in_hours
    
    return result

print(solution())