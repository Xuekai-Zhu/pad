def solution():
    """In the final game of the basketball season, four players scored points. Chandra scored twice as many points as did Akiko.
    Akiko scored 4 more points than did Michiko, and Michiko scored half as many points as did Bailey. 
    If Bailey scored 14 points, how many points in total did the team score in the final game of the season?"""
    # Define the number of points Bailey scored
    bailey_score = 14

    # Calculate Michiko's score
    michiko_score = bailey_score / 2

    # Calculate Akiko's score
    akiko_score = michiko_score + 4

    # Calculate Chandra's score
    chandra_score = akiko_score * 2

    # Calculate the total score of the team
    total_score = bailey_score + michiko_score + akiko_score + chandra_score

    result = total_score
    return result

print(solution())