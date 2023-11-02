def solution():
    
    total_groups = 9
    players_per_group = 4
    repeated_players = 3
    unique_players = total_groups * players_per_group - repeated_players
    result = unique_players
    return result

print(solution())