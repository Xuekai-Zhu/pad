def solution():
    games_first_round = 8
    games_second_round = 4
    games_third_round = 2
    games_fourth_round = 1
    cans_per_game = 5
    balls_per_can = 3
    total_balls = (games_first_round * cans_per_game * balls_per_can) + (games_second_round * cans_per_game * balls_per_can) + (games_third_round * cans_per_game * balls_per_can) + (games_fourth_round * cans_per_game * balls_per_can)
    result = total_balls
    return result

print(solution())