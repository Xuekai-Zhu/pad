def solution():
    initial_team_size = 25
    lost_members = 8
    new_members = 13
    current_team_size = initial_team_size - lost_members + new_members
    result = current_team_size
    return result

print(solution())