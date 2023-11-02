def solution():
    """In a Math competition, Sammy scored 20 points, Gab scored twice as many as Sammy's score, while Cher scored twice as many as Gab's score. If their opponent scored 85 points, how many more points do they have than their opponent?"""
    # Define the scores of Sammy, Gab, and Cher
    sammy_score = 20
    gab_score = sammy_score * 2
    cher_score = gab_score * 2

    # Calculate the total score of the team
    team_score = sammy_score + gab_score + cher_score

    # Calculate the difference between the team's score and their opponent's score
    score_difference = team_score - 85

    result = score_difference
    return result

print(solution())