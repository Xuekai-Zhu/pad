def solution():
    small_shirt_size = 3
    medium_shirt_size = 4
    large_shirt_size = 6

    num_small_shirts = 11
    num_medium_shirts = 8
    num_large_shirts = 6

    # Calculate the total area of all small shirts
    total_small_shirt_area = num_small_shirts * small_shirt_size

    # Calculate the total area of all medium shirts
    total_medium_shirt_area = num_medium_shirts * medium_shirt_size

    # Calculate the total area of all large shirts
    total_large_shirt_area = num_large_shirts * large_shirt_size

    # Calculate the total area of the quilt
    total_area = total_small_shirt_area + total_medium_shirt_area + total_large_shirt_area
    result = total_area
    return result

print(solution())