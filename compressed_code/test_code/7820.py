def solution():
    
    flights = 9
    height_per_flight = 10 * 12  
    step_height = 18
    total_steps = (flights * height_per_flight) // step_height
    result = total_steps
    return result

print(solution())