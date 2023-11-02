def solution():
    total_apples = 42
    number_of_crates = 12
    apples_per_crate = total_apples / number_of_crates
    rotten_apples = 4
    fresh_apples = apples_per_crate - rotten_apples
    apples_per_box = 10
    total_boxes = fresh_apples / apples_per_box
    result = total_boxes
    
    return result

print(solution())