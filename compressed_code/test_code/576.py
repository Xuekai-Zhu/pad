def solution():
    
    sandwiches = 8
    slices_per_sandwich = 2
    slices_per_pack = 4
    total_slices_needed = sandwiches * slices_per_sandwich
    packs_needed = (total_slices_needed + slices_per_pack - 1) // slices_per_pack
    result = packs_needed
    return result

print(solution())