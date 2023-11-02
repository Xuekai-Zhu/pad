def solution():
    
    starting_balls = 2
    games_per_worn_ball = 10
    games_per_lost_ball = 5
    games_per_canister = 4
    balls_per_canister = 3
    partner_balls = 1
    games_played = 20

    
    worn_balls = games_played // games_per_worn_ball

    
    lost_balls = games_played // games_per_lost_ball

    
    canisters_bought = games_played // games_per_canister

    
    balls_gained = canisters_bought * balls_per_canister

    
    total_balls = starting_balls + balls_gained - worn_balls - lost_balls - partner_balls

    result = total_balls
    return result

print(solution())