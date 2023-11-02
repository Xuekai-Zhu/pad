def solution():
    
    total_players = 50
    boys_ratio = 0.6
    girls_ratio = 1 - boys_ratio
    girls_count = int(girls_ratio * total_players)
    junior_girls_count = int(girls_count / 2)
    result = junior_girls_count
    return result

print(solution())