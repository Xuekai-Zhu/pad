def solution():
    
    madeline_grapes = 6
    brother_grapes = madeline_grapes * 5
    remaining_grapes = madeline_grapes - brother_grapes
    pies = 4
    grapes_per_pie = 12
    total_grapes = remaining_grapes + (pies * grapes_per_pie)
    result = total_grapes
    return result

print(solution())