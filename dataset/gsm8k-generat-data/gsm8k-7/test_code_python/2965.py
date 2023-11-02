def solution():
    initial_balls = 2
    games_per_worn_ball = 10
    games_per_lost_ball = 5
    games_per_canister = 4
    balls_per_canister = 3
    partner_balls = 1
    total_games = 20

    # Calculate the number of worn-out balls
    worn_out_balls = total_games // games_per_worn_ball

    # Calculate the number of lost balls
    lost_balls = total_games // games_per_lost_ball

    # Calculate the number of canisters bought
    canisters_bought = total_games // games_per_canister

    # Calculate the number of balls left after all the games
    remaining_balls = initial_balls - partner_balls - lost_balls + (canisters_bought * balls_per_canister) - worn_out_balls
    result = remaining_balls
    return result

print(solution())