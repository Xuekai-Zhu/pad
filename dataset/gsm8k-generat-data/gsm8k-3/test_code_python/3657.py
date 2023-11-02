def solution():
    """The Tampa Bay Bucs have 13 football players and 16 cheerleaders. If 10 football players and 4 cheerleaders quit, how many football players and cheerleaders are left?"""
    # Define the initial number of football players and cheerleaders
    initial_football_players = 13
    initial_cheerleaders = 16

    # Define the number of football players and cheerleaders who quit
    quitting_football_players = 10
    quitting_cheerleaders = 4

    # Calculate the remaining number of football players and cheerleaders
    remaining_football_players = initial_football_players - quitting_football_players
    remaining_cheerleaders = initial_cheerleaders - quitting_cheerleaders

    # Display the remaining number of football players and cheerleaders
    result = remaining_football_players, remaining_cheerleaders
    return result

print(solution())