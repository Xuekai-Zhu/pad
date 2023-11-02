def solution():
    """Betsy is sewing a quilt. The quilt is made up of 16 squares sewn together on one side and 16 squares sewn together on the other side. Betsy has already sewn 25% of the quilt together. How many more squares does she need to sew together?"""
    # Define the total number of squares in the quilt
    total_squares = 16 * 16

    # Calculate the number of squares Betsy has already sewn
    sewn_squares = total_squares * 0.25

    # Calculate the number of squares Betsy still needs to sew
    remaining_squares = total_squares - sewn_squares

    # return the result
    result = remaining_squares
    return result

print(solution())