def solution():
    slices_per_yogurt = 8  # Each yogurt is topped with 8 banana slices
    slices_per_banana = 10  # One banana will yield 10 slices
    yogurts_needed = 5  # Vivian needs to make 5 yogurts

    # Calculate the total number of banana slices needed
    total_slices_needed = slices_per_yogurt * yogurts_needed

    # Calculate the total number of bananas needed
    bananas_needed = total_slices_needed / slices_per_banana
    result = bananas_needed
    return result

print(solution())