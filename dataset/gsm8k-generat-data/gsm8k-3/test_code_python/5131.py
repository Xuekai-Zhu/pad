def solution():
    """Connor scored 2 in a game while Amy scored 4 more than Connor. Jason scored twice the score of Amy. If Connor, Amy, and Jason belong to the same team, how many points did their team have?"""
    # Define Connor's score
    connor_score = 2

    # Define Amy's score (4 more than Connor's score)
    amy_score = connor_score + 4

    # Define Jason's score (twice Amy's score)
    jason_score = amy_score * 2

    # Calculate the total score of the team
    total_score = connor_score + amy_score + jason_score

    # Display the total score of the team
    result = total_score
    return result

print(solution())