def solution():
    # Calculate the total number of squares in the quilt
    total_squares = 16 * 16

    # Calculate the number of squares Betsy has already sewn together
    sewn_squares = int(total_squares * 0.25)

    # Calculate the number of squares Betsy still needs to sew together
    remaining_squares = total_squares - sewn_squares

    result = remaining_squares
    return result

print(solution())