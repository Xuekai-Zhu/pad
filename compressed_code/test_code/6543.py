def solution():
    
    starting_floor = 9
    floors_down = 7
    floors_up1 = 3
    floors_up2 = 8
    final_floor = starting_floor - floors_down + floors_up1 + floors_up2
    total_floors = final_floor
    return total_floors

print(solution())