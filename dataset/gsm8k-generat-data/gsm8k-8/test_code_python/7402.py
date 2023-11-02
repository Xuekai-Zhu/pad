def solution():
    # Calculate the number of beacon towers
    num_towers = 7300 / 5

    # Calculate the number of soldiers per tower
    num_soldiers_per_tower = 2

    # Calculate the total number of soldiers
    total_soldiers = num_towers * num_soldiers_per_tower
    result = total_soldiers
    return result

print(solution())