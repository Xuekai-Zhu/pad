def solution():
    
    sandwiches = 8
    slices_per_sandwich = 2
    slices_needed = sandwiches * slices_per_sandwich
    slices_per_pack = 4
    packs_needed = slices_needed / slices_per_pack
    result = packs_needed
    return result

print(solution())