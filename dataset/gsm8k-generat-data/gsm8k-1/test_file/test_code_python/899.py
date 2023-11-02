def solution():
    """Jo has been making face masks. She can make 4 small masks with 2 yards of material and 3 large masks with 2.25 yards of material. How much material would she need to make 20 small and 8 large masks for her class?"""
    small_masks_per_yard = 4/2
    large_masks_per_yard = 3/2.25
    total_small_masks = 20
    total_large_masks = 8
    total_yards = (total_small_masks/small_masks_per_yard) + (total_large_masks/large_masks_per_yard)
    result = total_yards
    return result

print(solution())