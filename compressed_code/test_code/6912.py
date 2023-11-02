def solution():
    
    first_round = 8
    second_round = 4
    third_round = 2
    finals = 1
    total_games = first_round + second_round + third_round + finals
    cans_per_game = 5
    balls_per_can = 3
    total_balls = total_games * cans_per_game * balls_per_can
    result = total_balls
    return result

print(solution())