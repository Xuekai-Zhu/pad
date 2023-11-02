def solution():
    """Betsy is sewing a quilt. The quilt is made up of 16 squares sewn together on one side and 16 squares sewn together on the other side. Betsy has already sewn 25% of the quilt together. How many more squares does she need to sew together?"""
    total_squares = 16 * 16
    percent_sewn = 25
    squares_sewn = total_squares * (percent_sewn / 100)
    squares_left = total_squares - squares_sewn
    result = squares_left
    return result

print(solution())