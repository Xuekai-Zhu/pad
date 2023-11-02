def solution():
    games_played = 20
    balls_lost = 5
    balls_bought = 4
    balls_given = 1
    balls_at_start = 2
    balls_at_end = balls_at_start + balls_bought - balls_lost - balls_given
    result = balls_at_end
    return result

print(solution())