def solution():
    
    flight_distance = 10 * 12  
    step_length = 18  
    steps_per_flight = flight_distance / step_length
    total_steps = steps_per_flight * 9
    result = total_steps
    return result

print(solution())