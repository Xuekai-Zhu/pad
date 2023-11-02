def solution():
    
    slices_remaining = 0
    
    
    slices_remaining += 1  
    slices_remaining *= 2  
    slices_remaining *= 2  
    slices_remaining *= 2  
    
    
    slices_remaining -= 3  
    slices_remaining -= 2*2  
    
    result = slices_remaining
    return result

print(solution())