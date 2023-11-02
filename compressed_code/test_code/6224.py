def solution():
    
    num_teams = 4
    team_size = 10
    num_skates = num_teams * team_size * 2
    num_laces_per_skate = 3
    num_laces = num_skates * num_laces_per_skate
    result = num_laces
    return result

print(solution())