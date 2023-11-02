def solution():
    initial_bottles = 4 * 12  # Samira has 4 dozen water bottles to start with
    players = 11  # There are 11 players on the field
    bottles_per_player = 2  # Each player takes 2 bottles during the break
    end_game_bottles = 11  # Each player takes 1 more bottle at the end of the game

    # Calculate the total number of bottles used by the players
    total_bottles_used = players * (bottles_per_player + end_game_bottles)

    # Calculate the number of bottles remaining in Samira's box
    bottles_remaining = initial_bottles - total_bottles_used
    result = bottles_remaining
    return result

print(solution())