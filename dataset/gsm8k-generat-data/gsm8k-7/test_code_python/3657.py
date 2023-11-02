def solution():
    initial_num_players = 13
    initial_num_cheerleaders = 16

    num_players_quit = 10
    num_cheerleaders_quit = 4

    # Calculate the new number of football players
    num_players_left = initial_num_players - num_players_quit

    # Calculate the new number of cheerleaders
    num_cheerleaders_left = initial_num_cheerleaders - num_cheerleaders_quit

    result = (num_players_left, num_cheerleaders_left)
    return result

print(solution())