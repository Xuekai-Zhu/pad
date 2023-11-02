def solution():
    total_bottles = 10 * 20  # 10 cases of bottled water with 20 bottles in each case
    used_first_game = 70  # 70 bottles were used during the first game
    left_after_second_game = 20  # 20 bottles were left after the second game

    # Calculate how many bottles were used during the second game
    used_second_game = total_bottles - used_first_game - left_after_second_game
    result = used_second_game
    return result

print(solution())