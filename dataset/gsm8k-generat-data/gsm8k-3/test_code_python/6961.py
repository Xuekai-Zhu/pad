def solution():
    """A certain school bought 10 cases of bottled water for their athletes. There are 20 bottles in each case. Seventy bottles of water were used during the first game. After the second game, only 20 bottles of water were left. How many bottles of water were used during the second game?"""
    # Define the number of cases and bottles per case
    NUM_CASES = 10
    BOTTLES_PER_CASE = 20

    # Calculate the total number of bottles purchased
    total_bottles = NUM_CASES * BOTTLES_PER_CASE

    # Calculate the number of bottles used during the first game
    used_first_game = 70

    # Calculate the number of bottles remaining after the first game
    remaining_after_first_game = total_bottles - used_first_game

    # Calculate the number of bottles used during the second game
    used_second_game = remaining_after_first_game - 20

    # Display the number of bottles used during the second game
    result = used_second_game
    return result

print(solution())