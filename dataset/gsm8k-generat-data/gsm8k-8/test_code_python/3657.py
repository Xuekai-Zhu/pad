def solution():
    # Define the initial number of players and cheerleaders
    initial_players = 13
    initial_cheerleaders = 16

    # Define the number of players and cheerleaders who quit
    quitting_players = 10
    quitting_cheerleaders = 4

    # Calculate the remaining number of players and cheerleaders
    remaining_players = initial_players - quitting_players
    remaining_cheerleaders = initial_cheerleaders - quitting_cheerleaders

    # Calculate the total number of remaining players and cheerleaders
    total_remaining = remaining_players + remaining_cheerleaders
    result = total_remaining
    return result

print(solution())