def solution():
    initial_balls = 2  # Bertha starts with 2 balls
    games_played = 20  # Bertha plays 20 games

    # Calculate the number of balls worn out after 20 games
    balls_worn_out = games_played // 10

    # Calculate the number of balls lost after 20 games
    balls_lost = games_played // 5

    # Calculate the number of canisters of balls bought after 20 games
    canisters_bought = games_played // 4

    # Calculate the total number of balls after 20 games
    total_balls = initial_balls - 1 - balls_lost + canisters_bought * 3 - balls_worn_out

    result = total_balls
    return result

print(solution())