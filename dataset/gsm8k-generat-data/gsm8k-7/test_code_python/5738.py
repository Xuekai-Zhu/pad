def solution():
    num_goalies = 3
    num_defenders = 10
    num_midfielders = 2 * num_defenders
    total_players = 40

    # Calculate the total number of goalies, defenders, and midfielders
    total_gdm = num_goalies + num_defenders + num_midfielders

    # Calculate the number of strikers
    num_strikers = total_players - total_gdm
    result = num_strikers
    return result

print(solution())