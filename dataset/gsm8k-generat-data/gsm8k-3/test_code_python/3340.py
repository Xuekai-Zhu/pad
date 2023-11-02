def solution():
    """In a Math competition, Sammy scored 20 points, Gab scored twice as many as Sammy's score, while Cher scored twice as many as Gab's score. If their opponent scored 85 points, how many more points do they have than their opponent?"""
    # Define the scores for Sammy, Gab, and Cher
    sammy_score = 20
    gab_score = 2 * sammy_score
    cher_score = 2 * gab_score

    # Calculate the total score for the team
    total_score = sammy_score + gab_score + cher_score

    # Calculate the difference between the team's score and their opponent's score
    difference = total_score - 85

    # Display the difference in points
    result = difference
    return result

print(solution())