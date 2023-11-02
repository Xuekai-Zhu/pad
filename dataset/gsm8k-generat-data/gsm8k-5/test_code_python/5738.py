def solution():
    total_players = 40  # The team has 40 players

    # Calculate the number of midfielders based on the number of defenders
    num_defenders = 10
    num_midfielders = 2 * num_defenders

    # Calculate the number of strikers based on the total number of players and the number of goalies, defenders, and midfielders
    num_goalies = 3
    num_strikers = total_players - num_goalies - num_defenders - num_midfielders

    result = num_strikers
    return result

print(solution())