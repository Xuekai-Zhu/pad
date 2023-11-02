def solution():
    size_per_picture_1 = 8  # Each picture is 8 MB
    size_per_picture_2 = 6  # Each picture is now 6 MB

    # Calculate the number of pictures that can fit in the memory card with 8 MB per picture
    total_1 = 3000

    # Calculate the number of pictures that can fit in the memory card with 6 MB per picture
    total_2 = total_1 * (size_per_picture_1 / size_per_picture_2)
    result = total_2
    return result

print(solution())