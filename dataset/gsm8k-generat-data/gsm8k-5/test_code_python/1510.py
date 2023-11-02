def solution():
    total_players = 50
    boys = 0.6 * total_players
    girls = total_players - boys
    junior_girls = (1 / 2) * (girls / 2)
    result = junior_girls
    return result

print(solution())