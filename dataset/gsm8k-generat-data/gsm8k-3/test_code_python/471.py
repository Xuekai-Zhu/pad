def solution():
    """Earl started delivering newspapers on the first floor of a condominium building. He then went up 5 floors then went down 2 floors. He again went up 7 floors and found that he is 9 floors away from the top of the building. How many floors does the building have?"""
    # Define Earl's starting point
    starting_floor = 1

    # Define the number of floors Earl went up and down
    up1 = 5
    down1 = 2
    up2 = 7

    # Define Earl's position after each move
    pos1 = starting_floor + up1
    pos2 = pos1 - down1
    pos3 = pos2 + up2

    # Define the distance from Earl's final position to the top of the building
    distance_to_top = 9

    # Calculate the total number of floors in the building
    total_floors = pos3 + distance_to_top

    # Display the total number of floors
    result = total_floors
    return result

print(solution())