def solution():
    
    starting_slices = 3
    current_slices = 2
    eaten_slices = 2
    stole_slices = 5
    remaining_slices = starting_slices + current_slices - eaten_slices - stole_slices
    result = remaining_slices
    return result

print(solution())