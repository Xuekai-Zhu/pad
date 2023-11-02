def solution():
    """Henry had 33 games, and he gave five of them to Neil. Now Henry has 4 times more games than Neil. How many games did Neil have at first?"""
    henry_games = 33
    neil_games = (henry_games - 5) / 4
    result = neil_games
    return result

print(solution())