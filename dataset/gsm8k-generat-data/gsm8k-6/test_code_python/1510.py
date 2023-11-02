def solution():
    total_players = 50
    boys = int(total_players * 0.6)
    girls = total_players - boys
    junior_girls = int(girls/2)
    result = junior_girls
    return result

print(solution())