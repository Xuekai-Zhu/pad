def solution():
    # Calculate the current floor of the elevator
    current_floor = 9 - 7 + 3 + 8  # the elevator goes down 7 floors, then up 3 floors, then up 8 floors

    # Calculate the total number of floors in the building
    total_floors = current_floor + 1  # add 1 to account for the top floor
    result = total_floors
    return result

print(solution())