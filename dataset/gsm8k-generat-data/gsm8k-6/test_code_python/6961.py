def solution():
    # Calculate the total number of bottles of water the school bought
    total_bottles = 10 * 20  # 10 cases of bottled water, with 20 bottles in each case

    # Calculate the number of bottles of water used during the second game
    used_during_second_game = total_bottles - 70 - 20  # subtract the bottles used during the first game and the remaining bottles after the second game from the total

    result = used_during_second_game
    return result

print(solution())