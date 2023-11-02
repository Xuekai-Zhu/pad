def solution():
    
    pies = 2
    slices_per_pie = 8
    slices_eaten_by_rebecca = 1
    total_slices = pies * slices_per_pie
    remaining_slices = total_slices - slices_eaten_by_rebecca * pies
    remaining_slices *= 0.5
    remaining_slices -= 2
    result = remaining_slices
    return result

print(solution())