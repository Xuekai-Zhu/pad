def solution():
    # Calculate the current floor Earl is on after going up, then down, then up
    current_floor = 1 + 5 - 2 + 7  # Earl started on floor 1, went up 5, down 2, then up 7
    # Calculate the total number of floors in the building
    total_floors = current_floor + 9
    result = total_floors
    return result

print(solution())