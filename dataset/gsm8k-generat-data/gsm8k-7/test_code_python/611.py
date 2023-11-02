def solution():
    total_slices = 40
    # Lard cuts the pizza into 4 equal slices
    slices_per_half = total_slices // 2
    # Lard gives one of the slices to Jelly
    jelly_slice = slices_per_half // 2 - 1 # one slice falls off
    result = jelly_slice
    return result

print(solution())