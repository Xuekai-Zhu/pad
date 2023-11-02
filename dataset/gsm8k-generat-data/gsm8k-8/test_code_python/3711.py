def solution():
    # Define the number of apples and pears Katherine has
    apple_count = 4
    pear_count = 3 * apple_count

    # Calculate the total number of pieces of fruit Katherine has
    total_count = apple_count + pear_count + banana_count

    # Solve for the number of bananas
    banana_count = 21 - total_count
    result = banana_count
    return result

print(solution())