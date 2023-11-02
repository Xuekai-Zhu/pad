def solution():
    # Determine how many games Neil has after receiving 6 from Henry
    neil_games = 7 + 6  

    # Determine how many games Henry has now
    henry_games = neil_games * 4

    # Determine how many games Henry had at first
    initial_henry_games = henry_games - 6
    result = initial_henry_games
    return result

print(solution())