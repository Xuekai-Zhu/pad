def solution():
    num_rounds = 4
    first_round_games = 8
    second_round_games = 4
    third_round_games = 2
    finals_games = 1
    num_cans_per_game = 5
    num_tennis_balls_per_can = 3

    # Calculate the total number of games in the tournament
    total_games = first_round_games + second_round_games + third_round_games + finals_games

    # Calculate the total number of tennis balls used in the tournament
    total_tennis_balls = total_games * num_cans_per_game * num_tennis_balls_per_can
    result = total_tennis_balls
    return result

print(solution())