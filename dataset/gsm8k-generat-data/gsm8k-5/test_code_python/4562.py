def solution():
    num_holes = 8  # Maynard's dog dug 8 holes
    filled_percentage = 0.75  # Maynard filled in 75% of each hole
    num_filled_holes = int(num_holes * filled_percentage)  # Calculate the number of holes that were filled in
    num_unfilled_holes = num_holes - num_filled_holes  # Calculate the number of holes that remain unfilled
    result = num_unfilled_holes
    return result

print(solution())