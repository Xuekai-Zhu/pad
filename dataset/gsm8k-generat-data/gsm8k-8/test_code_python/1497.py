def solution():
    # Define the initial number of games Henry had
    henry_games = 33

    # Calculate the number of games Henry has after giving some to Neil
    henry_games -= 5

    # Calculate the number of games Neil has
    neil_games = henry_games / 4

    # Calculate the initial number of games Neil had
    initial_neil_games = neil_games + 5
    result = initial_neil_games
    return result

print(solution())