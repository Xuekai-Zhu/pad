def solution():
     total_bottles = 10 * 20
     bottles_used_first_game = 70
     bottles_left = total_bottles - bottles_used_first_game
     bottles_used_second_game = bottles_left - 20
    result = bottles_used_second_game
    return result

print(solution())