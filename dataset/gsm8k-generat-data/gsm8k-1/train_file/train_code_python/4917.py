def solution():
    """In the final game of the basketball season, four players scored points. Chandra scored twice as many points as did Akiko. Akiko scored 4 more points than did Michiko, and Michiko scored half as many points as did Bailey. If Bailey scored 14 points, how many points in total did the team score in the final game of the season?"""
    bailey_points = 14
    michiko_points = bailey_points / 2
    akiko_points = michiko_points + 4
    chandra_points = akiko_points * 2
    total_points = bailey_points + michiko_points + akiko_points + chandra_points
    result = total_points
    return result

print(solution())