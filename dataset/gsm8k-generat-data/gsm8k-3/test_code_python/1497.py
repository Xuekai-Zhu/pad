def solution():
    """Henry had 33 games, and he gave five of them to Neil. Now Henry has 4 times more games than Neil. How many games did Neil have at first?"""
    # Let's assume Neil had x games at first
    x = 0

    # After Henry gave Neil five of his games, he had 33-5=28 games left
    henry_games = 28

    # Now we know that Henry has 4 times more games than Neil, which means Henry has 4*(x+5) games
    # We can set up an equation to solve for x:
    # 4*(x+5) = henry_games
    # 4x + 20 = 28
    # 4x = 8
    # x = 2

    # Therefore, Neil had 2 games at first
    result = x
    return result

print(solution())