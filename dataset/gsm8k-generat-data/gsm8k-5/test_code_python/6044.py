def solution():
    total_holes_played = 9 * 18  # Tom played 9 rounds of golf, which means he played 18 holes each round
    total_strokes = total_holes_played * 4  # Tom took an average of 4 strokes per hole

    # Calculate the par score
    par_score = 3 * total_holes_played

    # Calculate how many strokes over par Tom was
    strokes_over_par = total_strokes - par_score
    result = strokes_over_par
    return result

print(solution())