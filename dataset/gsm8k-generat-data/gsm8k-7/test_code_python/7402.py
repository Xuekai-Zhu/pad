def solution():
    tower_distance = 5  # kilometers between each beacon tower
    wall_length = 7300  # kilometers
    num_soldiers_per_tower = 2

    # Calculate the total number of beacon towers on the Great Wall
    num_towers = wall_length / tower_distance

    # Calculate the total number of soldiers stationed in the beacon towers
    num_soldiers = num_towers * num_soldiers_per_tower
    result = num_soldiers
    return result

print(solution())