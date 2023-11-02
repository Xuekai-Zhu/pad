def solution():
    distance_between_towers = 5  # The distance between each beacon tower is 5 kilometers
    length_of_wall = 7300  # The length of the Great Wall is 7300 kilometers

    # Calculate the number of beacon towers along the Great Wall
    num_towers = length_of_wall / distance_between_towers

    # Calculate the total number of soldiers in the beacon towers
    num_soldiers = num_towers * 2

    result = num_soldiers
    return result

print(solution())