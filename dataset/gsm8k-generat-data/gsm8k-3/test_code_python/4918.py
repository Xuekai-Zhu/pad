def solution():
    """In the final game of the basketball season, four players scored points.  Chandra scored twice as many points as did Akiko.  Akiko scored 4 more points than did Michiko, and Michiko scored half as many points as did Bailey.  If Bailey scored 14 points, how many points in total did the team score in the final game of the season?"""
    # Calculate the number of points scored by Michiko
    michiko_points = 14 / 2

    # Calculate the number of points scored by Akiko
    akiko_points = michiko_points + 4

    # Calculate the number of points scored by Chandra
    chandra_points = akiko_points * 2

    # Calculate the total number of points scored by the team
    total_points = michiko_points + akiko_points + chandra_points + 14

    # Display the total number of points
    result = total_points
    return result

print(solution())