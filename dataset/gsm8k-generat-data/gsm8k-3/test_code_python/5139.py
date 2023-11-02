def solution():
    """Betsy is sewing a quilt.  The quilt is made up of 16 squares sewn together on one side and 16 squares sewn together on the other side.  Betsy has already sewn 25% of the quilt together.  How many more squares does she need to sew together?"""
    # Define the total number of squares in the quilt
    TOTAL_SQUARES = 16 * 16

    # Calculate the number of squares Betsy has already sewn together
    squares_sewn = int(TOTAL_SQUARES * 0.25)

    # Calculate the number of squares Betsy still needs to sew together
    squares_left = TOTAL_SQUARES - squares_sewn

    # Display the number of squares Betsy still needs to sew together
    result = squares_left
    return result

print(solution())