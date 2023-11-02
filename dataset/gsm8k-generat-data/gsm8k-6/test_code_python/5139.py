def solution():
    # Calculate the total number of squares in the quilt
    total_squares = 16 * 16
    
    # Calculate the number of squares Betsy has already sewn together
    squares_sewn = total_squares * 0.25
    
    # Calculate the number of squares Betsy still needs to sew together
    squares_left = total_squares - squares_sewn
    
    result = squares_left
    return result

print(solution())