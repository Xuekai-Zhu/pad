def solution():
    
    total_balls = 100
    given_away = total_balls / 2
    balls_remaining = total_balls - given_away
    containers = 5
    balls_per_container = balls_remaining / containers
    result = balls_per_container
    return result

print(solution())