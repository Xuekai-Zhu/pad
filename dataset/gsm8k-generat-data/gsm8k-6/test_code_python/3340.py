def solution():
    # Find the scores of Sammy, Gab, and Cher
    sammy_score = 20
    gab_score = 2 * sammy_score
    cher_score = 2 * gab_score

    # Calculate the total score of Sammy, Gab, and Cher
    total_score = sammy_score + gab_score + cher_score

    # Calculate the difference between their score and their opponent's score
    difference = total_score - 85
    result = difference
    return result

print(solution())