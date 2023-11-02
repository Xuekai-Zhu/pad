def solution():
    """An elevator is on the 9th floor. It goes down 7 floors, then up 3 floors, then up 8 floors. If the elevator is on the top floor, how many floors are there in the building?"""
    starting_floor = 9
    floors_down = 7
    floors_up1 = 3
    floors_up2 = 8
    final_floor = starting_floor - floors_down + floors_up1 + floors_up2
    total_floors = final_floor
    return total_floors

print(solution())