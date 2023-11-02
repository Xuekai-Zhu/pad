def solution():
    
    distance_westward = 80
    distance_northward = 150
    total_distance = distance_westward + distance_northward
    num_trains = 2
    distance_per_train = total_distance / num_trains
    result = distance_per_train
    return result

print(solution())