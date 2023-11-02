def solution():
    
    warehouse_length = 600
    warehouse_width = 400
    num_patrols = 10
    skipped_patrols = 2
    total_distance = (2 * warehouse_length) + (2 * warehouse_width)
    distance_per_patrol = total_distance * num_patrols - (skipped_patrols * total_distance)
    result = distance_per_patrol
    return result

print(solution())