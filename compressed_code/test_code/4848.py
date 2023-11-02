def solution():
    
    total_items = 13
    eraser = 1
    pens = (total_items - eraser) / 3 * 2
    pencils = (total_items - eraser - pens)
    result = pencils
    return result

print(solution())