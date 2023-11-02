def solution():
    """An elevator is on the 9th floor. It goes down 7 floors, then up 3 floors, then up 8 floors. If the elevator is on the top floor, how many floors are there in the building?"""
    # Define the starting floor and the movements of the elevator
    starting_floor = 9
    movements = [-7, 3, 8]

    # Calculate the final floor of the elevator
    final_floor = starting_floor + sum(movements)

    # Calculate the total number of floors in the building
    total_floors = final_floor + 1

    result = total_floors
    return result

print(solution())