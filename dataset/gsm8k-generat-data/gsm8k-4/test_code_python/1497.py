def solution():
    """Henry had 33 games, and he gave five of them to Neil. Now Henry has 4 times more games than Neil. How many games did Neil have at first?"""
    # Define the initial number of games Henry had
    henry_games = 33

    # Define the number of games Henry gave to Neil
    neil_games_received = 5

    # Calculate the number of games Neil has now
    neil_games_now = (henry_games - neil_games_received) / 5

    # Calculate the number of games Neil had at first
    neil_games_initial = neil_games_now / 4

    # Return the result
    result = neil_games_initial
    return result

print(solution())