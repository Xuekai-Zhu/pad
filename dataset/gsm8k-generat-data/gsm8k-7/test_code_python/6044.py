def solution():
    num_rounds = 9
    num_holes = 18
    par_value = 3
    average_strokes_per_hole = 4

    # Calculate the total number of strokes Tom took
    total_strokes = num_rounds * num_holes * average_strokes_per_hole

    # Calculate the total par value
    total_par = num_holes * par_value

    # Calculate the number of strokes over par
    strokes_over_par = total_strokes - total_par
    result = strokes_over_par
    return result

print(solution())