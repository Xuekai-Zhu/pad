def solution():
    """Henry had some games, and he gave six of them to Neil. Now, Henry has 4 times more games than Neil. If Neil had 7 games at first, how many games did Henry have at first?"""
    # Calculate the number of games Neil has now
    neil_games = 7 + 6

    # Calculate the number of games Henry has now
    henry_games = 4 * neil_games

    # Calculate the number of games Henry had at first
    initial_henry_games = henry_games + 6

    # Display the initial number of games Henry had
    result = initial_henry_games
    return result

print(solution())