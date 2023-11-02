def solution():
    
    apples_per_crate = 42
    crates_delivered = 12
    rotten_apples = 4
    total_apples = apples_per_crate * crates_delivered - rotten_apples
    boxes_needed = total_apples // 10
    result = boxes_needed
    return result

print(solution())