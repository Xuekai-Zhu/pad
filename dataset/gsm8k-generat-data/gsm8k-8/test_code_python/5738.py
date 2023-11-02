def solution():
    # Define the number of goalies and defenders
    num_goalies = 3
    num_defenders = 10

    # Calculate the number of midfielders
    num_midfielders = 2 * num_defenders

    # Calculate the total number of players
    total_players = num_goalies + num_defenders + num_midfielders + x

    # Calculate the number of strikers
    num_strikers = 40 - total_players
    result = num_strikers
    return result

print(solution())