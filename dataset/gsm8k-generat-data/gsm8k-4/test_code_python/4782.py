def solution():
    """Henry had some games, and he gave six of them to Neil. Now, Henry has 4 times more games than Neil. If Neil had 7 games at first, how many games did Henry have at first?"""
    
    # Define the initial number of games Neil had
    neil_games = 7
    
    # Calculate the total number of games after Henry gives 6 to Neil
    total_games = neil_games + 6
    
    # Calculate the number of games Henry has now, which is 4 times more than Neil
    henry_games = 4 * neil_games
    
    # Calculate the number of games Henry had initially
    henry_initial = henry_games + 6
    
    result = henry_initial
    return result

print(solution())