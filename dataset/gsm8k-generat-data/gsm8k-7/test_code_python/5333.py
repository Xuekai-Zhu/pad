def solution():
    num_bell_peppers = 5
    num_large_slices = 20

    # Calculate the total number of large slices of bell pepper
    total_large_slices = num_bell_peppers * num_large_slices

    # Calculate the number of smaller pieces per large slice
    num_smaller_pieces = 3

    # Calculate the total number of smaller pieces of bell pepper
    total_smaller_pieces = (total_large_slices / 2) * num_smaller_pieces

    # Add the total number of large slices and smaller pieces to get the total number of slices and pieces
    total_slices = total_large_slices + total_smaller_pieces
    result = total_slices
    return result

print(solution())