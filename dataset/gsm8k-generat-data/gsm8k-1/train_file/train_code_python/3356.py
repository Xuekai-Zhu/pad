def solution():
    """James buys 100 tennis balls and gives half of them away. The other half he puts into 5 large containers. How many tennis balls go in each container?"""
    total_balls = 100
    given_away = total_balls / 2
    balls_remaining = total_balls - given_away
    containers = 5
    balls_per_container = balls_remaining / containers
    result = balls_per_container
    return result

print(solution())