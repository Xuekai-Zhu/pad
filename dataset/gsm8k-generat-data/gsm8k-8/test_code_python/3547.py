def solution():
    # Define the size of the two largest vans
    largest_van = 8000
    second_largest_van = 8000

    # Calculate the size of the third van
    third_van = second_largest_van * 0.7

    # Calculate the total size of the three largest vans
    total_largest_vans = largest_van + second_largest_van + third_van

    # Calculate the size of the remaining three vans
    remaining_vans = total_largest_vans * 1.5

    # Calculate the total size of all six vans
    total_size = total_largest_vans + remaining_vans

    result = total_size
    return result

print(solution())