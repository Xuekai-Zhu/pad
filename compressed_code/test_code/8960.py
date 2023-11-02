def solution():
    
    slices_per_yogurt = 8
    slices_per_banana = 10
    yogurts_to_make = 5
    total_slices_needed = slices_per_yogurt * yogurts_to_make
    bananas_needed = total_slices_needed / slices_per_banana
    result = bananas_needed
    return result

print(solution())