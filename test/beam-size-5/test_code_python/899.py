def solution():
    
    small_masks = 20
    large_masks = 8
    small_masks_per_yard = 2
    large_masks_per_yard = 2.25
    small_masks_needed = small_masks / small_masks_per_yard
    large_masks_needed = large_masks / large_masks_per_yard
    total_material = (small_masks_needed * small_masks_per_yard) + (large_masks_needed * large_masks_per_yard)
    result = total_material
    return result

print(solution())