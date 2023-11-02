def solution():
    num_walls_dining = 1
    time_per_wall_dining = 2
    num_walls_living = 4

    # Calculate the total time Eric spent on the dining room
    total_time_dining = num_walls_dining * time_per_wall_dining

    # Calculate the total time Eric needs to spend on the living room
    total_time_living = total_time_dining * num_walls_living

    result = total_time_living
    return result

print(solution())