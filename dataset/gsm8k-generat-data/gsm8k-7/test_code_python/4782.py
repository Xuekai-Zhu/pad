def solution():
    # Start by determining how many games Henry has after giving 6 to Neil
    neil_games = 7
    henry_games = neil_games + 6

    # Use the fact that Henry has 4 times more games than Neil to set up an equation
    # Let x be the number of games Henry had at first
    # Then 4 * neil_games = x - 6 + 6 (since Henry gave 6 games to Neil)
    # Simplifying the equation gives 4 * neil_games = x
    x = 4 * neil_games

    # Finally, we can solve for x to get the number of games Henry had at first
    result = x
    return result

print(solution())