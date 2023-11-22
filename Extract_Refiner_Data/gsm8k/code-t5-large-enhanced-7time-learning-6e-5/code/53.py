def solution():
    
    bridge_limit = 5000
    driver_weight = 3755
    empty_truck_weight = 3755
    max_weight = bridge_limit - driver_weight - empty_truck_weight
    max_boxes = max_weight // 15
    result = max_boxes
    return result

print(solution())