def solution():
    sammy_score = 20
    gab_score = 2 * sammy_score
    cher_score = 2 * gab_score
    opponent_score = 85

    # Calculate the total points of Sammy, Gab, and Cher
    total_points = sammy_score + gab_score + cher_score

    # Calculate the difference between the total points of the three and their opponent
    difference = total_points - opponent_score
    result = difference
    return result

print(solution())