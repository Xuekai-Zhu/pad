def solution():
    balls = 100
    balls_given_away = balls / 2
    balls_remaining = balls - balls_given_away
    balls_per_container = balls_remaining / 5
    result = balls_per_container
    return result

print(solution())