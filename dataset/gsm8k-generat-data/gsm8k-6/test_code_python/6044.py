def solution():
    # Calculate the total number of strokes taken by Tom
    total_strokes = 9 * 4  # Tom plays 9 rounds of golf and takes an average of 4 strokes per hole

    # Calculate the total par value for 9 holes
    total_par = 9 * 3  # par value per hole is 3

    # Calculate the number of strokes over par
    strokes_over_par = total_strokes - total_par
    result = strokes_over_par
    return result

print(solution())