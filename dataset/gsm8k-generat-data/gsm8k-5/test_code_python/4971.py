def solution():
    total_matches = 8
    krishna_wins = 3/4 * total_matches
    callum_wins = total_matches - krishna_wins
    total_points = callum_wins * 10
    result = total_points
    return result

print(solution())