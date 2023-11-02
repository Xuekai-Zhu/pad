def solution():
    holes_played = 9
    strokes_per_hole = 4
    par_value = 3
    total_strokes = holes_played * strokes_per_hole
    strokes_over_par = total_strokes - (par_value * holes_played)
    result = strokes_over_par
    return result

print(solution())