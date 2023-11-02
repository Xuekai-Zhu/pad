def solution():
    """Each yogurt is topped with 8 banana slices. One banana will yield 10 slices. If Vivian needs to make 5 yogurts, how many bananas does she need to buy?"""
    slices_per_yogurt = 8
    slices_per_banana = 10
    yogurts_to_make = 5
    total_slices_needed = slices_per_yogurt * yogurts_to_make
    bananas_needed = total_slices_needed / slices_per_banana
    result = bananas_needed
    return result

print(solution())