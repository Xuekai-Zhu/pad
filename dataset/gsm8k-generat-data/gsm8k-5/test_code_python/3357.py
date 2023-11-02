def solution():
    total_balls = 100  # James buys 100 tennis balls
    half_balls = total_balls / 2  # James gives away half of the tennis balls
    remaining_balls = total_balls - half_balls  # James has the other half left

    # Calculate the number of tennis balls in each container
    balls_per_container = remaining_balls / 5
    result = balls_per_container
    return result

print(solution())