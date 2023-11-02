def solution():
    
    num_cakes = 2
    cake_slices = 8
    slices_given_away = (num_cakes * cake_slices) // 4
    slices_remaining = (num_cakes * cake_slices) - slices_given_away
    slices_given_to_family = slices_remaining // 3
    slices_remaining -= slices_given_to_family
    slices_remaining -= 3  
    result = slices_remaining
    return result

print(solution())