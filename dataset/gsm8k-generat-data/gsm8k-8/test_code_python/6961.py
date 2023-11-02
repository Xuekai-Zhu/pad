def solution():
    # Calculate the total number of bottles of water purchased
    total_bottles = 10 * 20

    # Calculate the number of bottles used during the first game
    first_game_bottles = 70

    # Calculate the number of bottles left after the first game
    bottles_left = total_bottles - first_game_bottles

    # Calculate the number of bottles used during the second game
    second_game_bottles = bottles_left - 20
    result = second_game_bottles
    return result

print(solution())