def solution():
    num_bread_slices = 2
    num_tears_per_slice = 2

    # Calculate the total number of bread pieces after tearing each slice in half twice
    total_bread_pieces = num_bread_slices * (num_tears_per_slice ** 2)
    result = total_bread_pieces
    return result

print(solution())