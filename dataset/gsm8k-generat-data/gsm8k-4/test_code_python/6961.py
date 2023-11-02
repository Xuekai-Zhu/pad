def solution():
    """A certain school bought 10 cases of bottled water for their athletes. There are 20 bottles in each case. Seventy bottles of water were used during the first game. After the second game, only 20 bottles of water were left. How many bottles of water were used during the second game?"""
    # Define the initial number of bottles
    initial_bottles = 10 * 20

    # Calculate the number of bottles used during the first game
    used_first_game = 70

    # Calculate the number of bottles left after the first game
    left_after_first_game = initial_bottles - used_first_game

    # Calculate the number of bottles left after the second game
    left_after_second_game = 20

    # Calculate the number of bottles used during the second game
    used_second_game = left_after_first_game - left_after_second_game

    result = used_second_game
    return result

print(solution())