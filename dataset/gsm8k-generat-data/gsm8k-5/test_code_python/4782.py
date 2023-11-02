def solution():
    neil_games = 7  # Neil had 7 games at first
    henry_games = (neil_games + 6) * 4  # Henry has 4 times more games than Neil after giving him 6 games
    initial_total = neil_games + henry_games - 6  # Subtract 6 since Henry gave 6 games to Neil

    result = initial_total
    return result

print(solution())