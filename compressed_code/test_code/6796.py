def solution():
    
    green_ratio = 2 
    total_ratio = 1 + green_ratio + 5 
    green_paint = 6 
    total_paint = green_paint * (total_ratio / green_ratio) 
    
    result = total_paint
    return result

print(solution())