def solution():
    total_slices = 16  # The box of pizza is cut into 16 slices
    slices_eaten = total_slices * 3 / 4  # Three-fourths of the pizza was eaten by the family
    slices_left = total_slices - slices_eaten  # Calculate the number of slices left
    result = slices_left
    return result

print(solution())