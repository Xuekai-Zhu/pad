def solution():
    # Calculate the number of matches Krishna won
    krishna_wins = 3/4 * 8
    # Calculate the number of matches Callum won
    callum_wins = 8 - krishna_wins
    # Calculate the total number of points Callum earned
    callum_points = callum_wins * 10
    result = callum_points
    return result

print(solution())