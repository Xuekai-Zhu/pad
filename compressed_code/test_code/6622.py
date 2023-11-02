def solution():
    
    apples_per_crate = 180
    total_crates = 12
    rotten_apples = 160
    usable_apples = (apples_per_crate * total_crates) - rotten_apples
    boxes = usable_apples / 20
    result = boxes
    
    return result

print(solution())