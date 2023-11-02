def solution():
    
    apples_per_crate = 180
    num_crates = 12
    num_rotten = 160
    num_good_apples = (apples_per_crate * num_crates) - num_rotten
    num_boxes = num_good_apples // 20
    result = num_boxes
    return result

print(solution())