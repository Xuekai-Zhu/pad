def solution():
    """Krishna and Callum are playing a game where they earn 10 points if they win any round. If they played eight matches and Krishna won 3/4 of the matches, what is the total number of points that Callum earned?"""
    # Define the number of matches played
    matches_played = 8

    # Define the number of matches won by Krishna
    krishna_wins = matches_played * (3/4)

    # Define the number of matches won by Callum
    callum_wins = matches_played - krishna_wins

    # Calculate the total number of points earned by Callum
    callum_points = callum_wins * 10

    # Display the total number of points earned by Callum
    result = callum_points
    return result

print(solution())