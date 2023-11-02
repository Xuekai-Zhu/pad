def solution():
    team_1_2_pointers = 25
    team_1_3_pointers = 8
    team_1_free_throws = 10
    team_2_2_pointers = team_1_2_pointers * 2
    team_2_3_pointers = team_1_3_pointers / 2
    team_2_free_throws = team_1_free_throws / 2
    team_1_points = team_1_2_pointers + (team_1_3_pointers * 3) + (team_1_free_throws * 1)
    team_2_points = team_2_2_pointers + (team_2_3_pointers * 3) + (team_2_free_throws * 1)
    total_points = team_1_points + team_2_points
    result = total_points
    return result

print(solution())