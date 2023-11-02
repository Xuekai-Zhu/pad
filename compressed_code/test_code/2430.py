def solution():
    
    pizza_slices = 8
    angeli_slices = 3/2
    marlon_slices = 3/2
    total_slices_eaten = angeli_slices + marlon_slices
    slices_left = pizza_slices - total_slices_eaten
    result = slices_left
    return result

print(solution())