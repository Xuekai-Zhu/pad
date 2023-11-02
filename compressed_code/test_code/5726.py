def solution():
    
    tower_distance = 5
    wall_length = 7300
    num_towers = wall_length // tower_distance
    num_soldiers = num_towers * 2
    result = num_soldiers
    return result

print(solution())