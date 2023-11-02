def solution():
    """James buys 100 tennis balls and gives half of them away. The other half he puts into 5 large containers. How many tennis balls go in each container?"""
    # Define the initial number of tennis balls
    initial_balls = 100

    # Calculate the number of tennis balls he keeps after giving half away
    remaining_balls = initial_balls / 2

    # Calculate the number of tennis balls in each container
    balls_per_container = remaining_balls / 5

    # Return the result
    result = balls_per_container
    return result

print(solution())