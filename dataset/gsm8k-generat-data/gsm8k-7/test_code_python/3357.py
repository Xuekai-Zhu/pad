def solution():
    num_tennis_balls = 100
    num_containers = 5

    # Calculate the number of tennis balls that James keeps for himself
    num_kept_balls = num_tennis_balls / 2

    # Calculate the number of tennis balls that James puts in each container
    num_balls_per_container = num_kept_balls / num_containers
    result = num_balls_per_container
    return result

print(solution())