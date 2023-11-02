def solution():
    current_floor = 9
    floors_down = 7
    floors_up_1 = 3
    floors_up_2 = 8
    top_floor = current_floor - floors_down + floors_up_1 + floors_up_2
    num_floors = top_floor
    return num_floors

print(solution())