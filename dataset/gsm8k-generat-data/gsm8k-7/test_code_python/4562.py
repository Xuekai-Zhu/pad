def solution():
    num_holes = 8
    fill_percentage = 0.75

    # Calculate the number of holes that were filled
    num_filled_holes = num_holes * fill_percentage

    # Calculate the number of holes that remain unfilled
    num_unfilled_holes = num_holes - num_filled_holes
    result = num_unfilled_holes
    return result

print(solution())