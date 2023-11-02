def solution():
    
    suki_bags = 6.5
    suki_bag_weight = 22
    jimmy_bags = 4.5
    jimmy_bag_weight = 18
    combined_weight = (suki_bags * suki_bag_weight) + (jimmy_bags * jimmy_bag_weight)
    container_size = 8
    num_containers = combined_weight / container_size
    result = num_containers
    return result

print(solution())