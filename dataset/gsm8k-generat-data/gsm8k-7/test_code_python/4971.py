def solution():
    total_matches = 8
    krishna_won = 3/4 * total_matches
    callum_won = total_matches - krishna_won
    points_per_match = 10

    # Calculate the total points earned by Callum
    callum_points = callum_won * points_per_match
    result = callum_points
    return result

print(solution())