def solution():
    
    initial_team_size = 25
    people_quit = 8
    new_people_join = 13
    current_team_size = initial_team_size - people_quit + new_people_join
    result = current_team_size
    return result

print(solution())