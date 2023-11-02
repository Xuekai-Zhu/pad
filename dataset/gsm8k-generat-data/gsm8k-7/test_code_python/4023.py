def solution():
    banana_slices_per_yogurt = 8
    slices_per_banana = 10
    num_yogurts = 5

    # Calculate the total number of banana slices needed
    total_banana_slices = banana_slices_per_yogurt * num_yogurts

    # Calculate the number of bananas needed
    num_bananas = total_banana_slices / slices_per_banana
    result = num_bananas
    return result

print(solution())