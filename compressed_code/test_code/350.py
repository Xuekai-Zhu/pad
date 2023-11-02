def solution():
    
    initial_team_size = 25
    quit_size = 8
    new_size = 13
    current_team_size = initial_team_size - quit_size + new_size
    result = current_team_size
    return result

print(solution())