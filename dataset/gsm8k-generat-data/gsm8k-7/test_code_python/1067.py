def solution():
    apples_per_crate = 180
    num_crates = 12
    num_rotten = 160
    apples_remaining = (apples_per_crate * num_crates) - num_rotten
    apples_per_box = 20
    num_boxes = apples_remaining / apples_per_box
    result = num_boxes
    return result

print(solution())