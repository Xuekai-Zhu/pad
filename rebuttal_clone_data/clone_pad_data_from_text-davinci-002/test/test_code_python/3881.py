def solution():
    total_players = 1000
    players_between_25_35 = total_players * 2 / 5
    players_older_than_35 = total_players * 3 / 8
    players_younger_than_25 = total_players - players_between_25_35 - players_older_than_35
    result = players_younger_than_25
    return result

print(solution())