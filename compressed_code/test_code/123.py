def solution():
    
    distance_to_destination = 55
    distance_to_starting_point = distance_to_destination + 10
    total_distance = distance_to_destination + distance_to_starting_point
    driving_time = (total_distance * 2) / 60
    total_time = driving_time + 2
    result = total_time
    return result

print(solution())