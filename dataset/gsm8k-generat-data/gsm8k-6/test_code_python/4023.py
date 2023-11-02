def solution():
    # Calculate the total number of banana slices needed for 5 yogurts
    total_slices = 5 * 8  # each yogurt is topped with 8 banana slices
    bananas_needed = (total_slices / 10) + 1  # one banana yields 10 slices, round up to the nearest banana
    result = bananas_needed
    return result

print(solution())