def solution():
    """Krishna and Callum are playing a game where they earn 10 points if they win any round. If they played eight matches and Krishna won 3/4 of the matches, what is the total number of points that Callum earned?"""
    # Define the total number of matches
    total_matches = 8

    # Calculate the number of matches Krishna won
    krishna_wins = total_matches * 3/4

    # Calculate the number of matches Callum won
    callum_wins = total_matches - krishna_wins

    # Calculate the total number of points Callum earned
    callum_points = callum_wins * 10

    # return the result
    result = callum_points
    return result

print(solution())