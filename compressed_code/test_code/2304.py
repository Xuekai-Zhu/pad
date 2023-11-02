def solution():
    
    starting_balls = 2
    games_played = 20
    balls_lost = games_played // 5
    balls_worn_out = games_played // 10
    canisters_bought = games_played // 4
    balls_from_canisters = canisters_bought * 3
    total_balls = starting_balls - 1 + balls_from_canisters - balls_lost - balls_worn_out
    result = total_balls
    return result

print(solution())