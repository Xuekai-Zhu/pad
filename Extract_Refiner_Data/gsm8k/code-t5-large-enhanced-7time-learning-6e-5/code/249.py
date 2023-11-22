def solution():
    
    starting_floor = 3
    elevator_floor = 4 * starting_floor + 6
    current_floor = starting_floor + elevator_floor
    result = current_floor
    return result

print(solution())