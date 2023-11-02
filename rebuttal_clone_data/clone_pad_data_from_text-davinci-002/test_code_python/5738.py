def solution():
    total_players = 40
    num_goalies = 3
    num_defenders = 10
    num_midfielders = num_defenders * 2
    num_strikers = total_players - num_goalies - num_defenders - num_midfielders
    result = num_strikers
    return result

print(solution())