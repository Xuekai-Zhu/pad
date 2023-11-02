def solution():
    # Define the number of holes and the fill percentage
    num_holes = 8
    fill_percentage = 0.75

    # Calculate the number of holes that remain unfilled
    num_unfilled_holes = num_holes - (num_holes * fill_percentage)
    result = num_unfilled_holes
    return result

print(solution())