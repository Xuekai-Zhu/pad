def solution():
    # Define the number of rounds played and average strokes per hole
    rounds_played = 9
    strokes_per_hole = 4

    # Calculate the total number of strokes taken
    total_strokes = rounds_played * 18 * strokes_per_hole

    # Calculate the total par value
    total_par = rounds_played * 18 * 3

    # Calculate the number of strokes over par
    strokes_over_par = total_strokes - total_par
    result = strokes_over_par
    return result

print(solution())