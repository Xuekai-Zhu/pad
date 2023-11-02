def solution():
    sammy_score = 20  # Sammy scored 20 points
    gab_score = 2 * sammy_score  # Gab scored twice as many as Sammy's score
    cher_score = 2 * gab_score  # Cher scored twice as many as Gab's score
    total_score = sammy_score + gab_score + cher_score  # Calculate the total score
    opponent_score = 85  # Their opponent scored 85 points
    difference = total_score - opponent_score  # Calculate the difference in scores
    result = difference
    return result

print(solution())