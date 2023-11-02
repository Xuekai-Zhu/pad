def solution():
    apples_per_crate = 42
    num_crates = 12
    rotten_apples = 4
    apples_remaining = (apples_per_crate * num_crates) - rotten_apples
    apples_per_box = 10
    num_boxes = apples_remaining // apples_per_box  # Floor division to get integer value
    result = num_boxes
    return result

print(solution())