def solution():
    """Betsy is sewing a quilt. The quilt is made up of 16 squares sewn together on one side and 16 squares sewn together on the other side. Betsy has already sewn 25% of the quilt together. How many more squares does she need to sew together?"""
    total_squares = 16 * 16
    sewn_squares = total_squares * 0.25
    remaining_squares = total_squares - sewn_squares
    result = remaining_squares
    return result

print(solution())