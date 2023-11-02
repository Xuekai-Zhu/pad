def solution():
    num_cases = 10
    bottles_per_case = 20

    # Calculate the total number of bottles of water bought
    total_bottles = num_cases * bottles_per_case

    # Calculate the number of bottles of water used during the first game
    used_first_game = 70

    # Calculate the total number of bottles of water remaining after the first game
    remaining_after_first_game = total_bottles - used_first_game

    # Calculate the number of bottles of water used during the second game
    used_second_game = remaining_after_first_game - 20
    result = used_second_game
    return result

print(solution())