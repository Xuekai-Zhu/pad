def solution():
    
    apples_per_crate = 42
    num_crates = 12
    num_rotten_apples = 4
    total_apples = apples_per_crate * num_crates - num_rotten_apples
    num_boxes = total_apples // 10
    result = num_boxes
    return result

print(solution())