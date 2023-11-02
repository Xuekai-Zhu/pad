def solution():
    initial_team_size = 25
    people_who_quit = 8
    people_who_joined = 13
    current_team_size = initial_team_size + people_who_joined - people_who_quit
    result = current_team_size
    return result

print(solution())