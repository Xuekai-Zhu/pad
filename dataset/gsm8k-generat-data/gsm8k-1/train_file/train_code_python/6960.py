def solution():
    """A certain school bought 10 cases of bottled water for their athletes. There are 20 bottles in each case. Seventy bottles of water were used during the first game. After the second game, only 20 bottles of water were left. How many bottles of water were used during the second game?"""
    cases_bought = 10
    bottles_per_case = 20
    total_bottles = cases_bought * bottles_per_case
    bottles_used_first_game = 70
    bottles_left_after_first_game = total_bottles - bottles_used_first_game
    bottles_left_after_second_game = 20
    bottles_used_second_game = total_bottles - bottles_used_first_game - bottles_left_after_second_game
    result = bottles_used_second_game
    return result

print(solution())