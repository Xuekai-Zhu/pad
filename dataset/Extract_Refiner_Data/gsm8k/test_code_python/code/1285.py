def solution():
    
    # Define the size of each t-shirt
    SMALL_SHIRT_SIZE = 3
    MEDIUM_SHIRT_SIZE = 4
    LARGE_SHIRT_SIZE = 6

    # Define the number of small, medium, and large t-shirts used
    small_shirts = 11
    medium_shirts = 8
    large_shirts = 6

    # Calculate the total size of the shirts
    total_size = (small_shirts * SMALL_SHIRT_SIZE) + (medium_shirts * MEDIUM_SHIRT_SIZE) + (large_shirts * LARGE_SHIRT_SIZE)

    # Display the total size of the quilt
    result = total_size
    return result

print(solution())