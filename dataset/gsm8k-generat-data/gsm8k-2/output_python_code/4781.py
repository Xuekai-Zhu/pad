def solution():
    """Henry had some games, and he gave six of them to Neil. Now, Henry has 4 times more games than Neil. If Neil had 7 games at first, how many games did Henry have at first?"""
    neil_games = 7
    henry_games = (neil_games + 6) * 4
    initial_total_games = neil_games + henry_games - 6
    result = initial_total_games
    return result

print(solution())