def solution():
    
    total_players = 50
    boys_percentage = 60
    girls_percentage = 100 - boys_percentage
    girls_total = (girls_percentage / 100) * total_players
    junior_girls = girls_total / 2
    result = junior_girls
    return result

print(solution())