def solution():
    # Calculate the total number of slices
    total_slices = 8 + 14 
    
    # Calculate the slices already eaten
    eaten_slices = 9 + 9
    
    # Calculate the slices remaining
    remaining_slices = total_slices - eaten_slices
    
    # Calculate the number of slices per person
    slices_per_person = remaining_slices / 2
    
    result = slices_per_person
    return result

print(solution())