def solution():
    # Calculate the total points Liz scores
    free_throws = 5 * 1
    three_pointers = 3 * 3
    jump_shots = 4 * 2
    liz_score = free_throws + three_pointers + jump_shots

    # Calculate the total points the other team scores
    other_team_score = 10

    # Calculate Liz's team's final score
    liz_team_score = liz_score + other_team_score

    # Calculate the point differential
    point_diff = liz_team_score - (20 * 3)

    result = point_diff
    return result

print(solution())