def solution():
    """An elevator is on the 9th floor. It goes down 7 floors, then up 3 floors, then up 8 floors. If the elevator is on the top floor, how many floors are there in the building?"""
    # Starting floor of the elevator
    floor = 9

    # Go down 7 floors
    floor -= 7

    # Go up 3 floors
    floor += 3

    # Go up 8 floors
    floor += 8

    # Final floor of the elevator
    final_floor = floor

    # Number of floors in the building
    num_floors = final_floor + 1

    # Display the number of floors
    result = num_floors
    return result

print(solution())