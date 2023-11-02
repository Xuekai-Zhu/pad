def solution():
    # Start at 9th floor
    current_floor = 9

    # Go down 7 floors
    current_floor -= 7

    # Go up 3 floors
    current_floor += 3

    # Go up 8 floors
    current_floor += 8

    # The elevator is on the top floor
    # Calculate the total number of floors in the building 
    total_floors = current_floor + 1
    result = total_floors
    return result

print(solution())