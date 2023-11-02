def solution():
    
    total_ribbon = 4.5
    ribbon_per_box = 0.7
    leftover_ribbon = 1
    boxes_tied = (total_ribbon - leftover_ribbon) / ribbon_per_box
    result = boxes_tied
    return result

print(solution())