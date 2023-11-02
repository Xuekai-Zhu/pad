def solution():
    Washington_to_Idaho = 640
    Idaho_to_Nevada = 550
    speed_to_Idaho = 80
    speed_from_Idaho = 50
    hours_to_Idaho = Washington_to_Idaho / speed_to_Idaho
    hours_from_Idaho = Idaho_to_Nevada / speed_from_Idaho
    total_hours = hours_to_Idaho + hours_from_Idaho
    
    result = total_hours
    return result

print(solution())