def solution():
    # Define the number of slices per banana and the number of yogurts needed
    slices_per_banana = 10
    num_yogurts = 5

    # Calculate the total number of banana slices needed
    total_slices = slices_per_banana * 8 * num_yogurts

    # Calculate the number of bananas needed
    bananas_needed = total_slices / slices_per_banana
    result = bananas_needed
    return result

print(solution())