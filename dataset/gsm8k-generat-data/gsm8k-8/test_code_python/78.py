def solution():
    # Calculate the total number of slices in the cookie pies
    total_slices = 3 * 10
    
    # Calculate the total number of people who had a slice
    total_people = 24 + 1
    
    # Calculate the total number of slices eaten
    total_slices_eaten = total_people
    
    # Calculate the number of slices left
    slices_left = total_slices - total_slices_eaten
    result = slices_left
    return result

print(solution())