def solution():
    
    total_holes = 8
    filled_percentage = 0.75
    filled_holes = total_holes * filled_percentage
    unfilled_holes = total_holes - filled_holes
    result = unfilled_holes
    return result

print(solution())