def solution():
    
    total_players = 40
    goalies = 3
    defenders = 10
    midfielders = 2 * defenders
    remaining_players = total_players - goalies - defenders - midfielders
    strikers = remaining_players
    result = strikers
    return result

print(solution())