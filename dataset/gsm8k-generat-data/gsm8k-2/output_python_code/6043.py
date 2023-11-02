def solution():
    """Tom plays 9 rounds of golf. He takes an average of 4 strokes per hole. The par value per hole is 3. How many strokes over par was he?"""
    holes_per_round = 18
    rounds = 9
    par_value = 3
    total_strokes = rounds * holes_per_round * 4
    par_score = rounds * holes_per_round * par_value
    over_par = total_strokes - par_score
    result = over_par
    return result

print(solution())