def solution():
    """Each yogurt is topped with 8 banana slices.  One banana will yield 10 slices.  If Vivian needs to make 5 yogurts, how many bananas does she need to buy?"""
    # Define the number of banana slices per yogurt
    slices_per_yogurt = 8

    # Define the number of slices per banana
    slices_per_banana = 10

    # Calculate the total number of banana slices needed for all the yogurts
    total_slices_needed = slices_per_yogurt * 5

    # Calculate the total number of bananas needed
    bananas_needed = total_slices_needed / slices_per_banana

    # Round up the number of bananas needed to the nearest integer
    bananas_needed = math.ceil(bananas_needed)

    # Display the number of bananas needed
    result = bananas_needed
    return result

print(solution())