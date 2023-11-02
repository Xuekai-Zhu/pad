def solution():
    # Find the number of games Neil has after Henry gave him 5 games
    neil_games = 5  

    # Find the number of games Henry has after giving 5 games to Neil
    henry_games = 33 - 5  

    # Find the number of games Neil had at first
    neil_games_at_first = (henry_games / 4) - neil_games
    result = neil_games_at_first
    return result

print(solution())