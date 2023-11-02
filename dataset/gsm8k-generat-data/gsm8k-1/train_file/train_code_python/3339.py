def solution():
    """In a Math competition, Sammy scored 20 points, Gab scored twice as many as Sammy's score, while Cher scored twice as many as Gab's score. If their opponent scored 85 points, how many more points do they have than their opponent?"""
    sammy_score = 20
    gab_score = sammy_score * 2
    cher_score = gab_score * 2
    total_score = sammy_score + gab_score + cher_score
    opponent_score = 85
    difference = total_score - opponent_score
    result = difference
    return result

print(solution())