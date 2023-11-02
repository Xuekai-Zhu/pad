def solution():
    
    total_slices = 8
    doxa_slices = 1
    sister_slices = doxa_slices + 1
    brother_slices = sister_slices + 1
    total_slices_eaten = doxa_slices + sister_slices + brother_slices
    result = total_slices_eaten
    return result

print(solution())