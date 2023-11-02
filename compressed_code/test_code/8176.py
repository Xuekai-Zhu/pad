def solution():
    
    guests = 8
    slices_per_guest = 2
    total_slices_needed = guests * slices_per_guest
    slices_per_cake = 6
    cakes_baked = 4
    total_slices = slices_per_cake * cakes_baked
    slices_left = total_slices - (total_slices_needed + 3)
    result = slices_left
    return result

print(solution())