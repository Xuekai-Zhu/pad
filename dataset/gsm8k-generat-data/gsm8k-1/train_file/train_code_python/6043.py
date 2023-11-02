def solution():
    """Tom plays 9 rounds of golf. He takes an average of 4 strokes per hole. The par value per hole is 3. How many strokes over par was he?"""
    rounds = 9
    holes_per_round = 18
    par_value = 3
    average_strokes = 4
    total_strokes = rounds * holes_per_round * average_strokes
    total_par = rounds * holes_per_round * par_value
    strokes_over_par = total_strokes - total_par
    result = strokes_over_par
    return result

print(solution())