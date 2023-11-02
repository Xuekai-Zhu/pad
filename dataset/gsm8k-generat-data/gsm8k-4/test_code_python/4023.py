def solution():
    """Each yogurt is topped with 8 banana slices.  One banana will yield 10 slices.  If Vivian needs to make 5 yogurts, how many bananas does she need to buy?"""
    # Define the number of yogurt Vivian needs to make
    yogurt_count = 5

    # Calculate the total number of banana slices needed
    banana_slices_needed = yogurt_count * 8

    # Calculate the number of bananas needed
    bananas_needed = banana_slices_needed / 10

    # Round up to the nearest integer
    bananas_needed = math.ceil(bananas_needed)

    result = bananas_needed
    return result

print(solution())