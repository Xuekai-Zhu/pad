def solution():
    """Henry had 33 games, and he gave five of them to Neil. Now Henry has 4 times more games than Neil. How many games did Neil have at first?"""
    henrys_games = 33
    neils_games = (henrys_games - 5) / 4
    neils_initial_games = neils_games + 5
    result = neils_initial_games
    
    return result

print(solution())