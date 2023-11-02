def solution():
    
    pies = 2
    slices_per_pie = 8
    rebecca_slices = 2
    remaining_slices = (pies * slices_per_pie) - rebecca_slices
    remaining_slices *= 0.5
    remaining_slices -= 2
    result = remaining_slices
    return result

print(solution())