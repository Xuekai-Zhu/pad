def solution():
    """Emma bought a loaf of bread that had a certain number of slices. 
    Her little cousin Andy ate 3 slices from the bread at two different points in time, 
    and then Emma decided she would make toast with the remaining slices. 
    If she uses 2 slices of bread to make 1 piece of toast bread, 
    how many slices were in the original loaf if she was able to make 10 pieces of toast bread and had 1 slice of bread left?"""
    
    # Calculate the total number of slices of bread
    total_slices = 2 * 10 + 1 + 3
    
    # Calculate the number of slices in the original loaf
    original_slices = total_slices + 2

    # Display the number of slices in the original loaf
    result = original_slices
    return result

print(solution())