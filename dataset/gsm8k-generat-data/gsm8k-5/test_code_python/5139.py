def solution():
    total_squares = 16 * 16  # The quilt is made up of 16 squares sewn together on each side
    completed_squares = total_squares * 0.25  # Betsy has already sewn 25% of the quilt
    remaining_squares = total_squares - completed_squares  # Betsy still needs to sew the remaining squares

    result = remaining_squares
    return result

print(solution())