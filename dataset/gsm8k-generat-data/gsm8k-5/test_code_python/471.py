def solution():
    current_floor = 1  # Earl starts at the first floor
    current_floor += 5  # Earl goes up 5 floors
    current_floor -= 2  # Earl goes down 2 floors
    current_floor += 7  # Earl goes up 7 floors
    floors_remaining = 9  # Earl is 9 floors away from the top of the building

    # Calculate the total number of floors in the building
    total_floors = current_floor + floors_remaining
    result = total_floors
    return result

print(solution())