def solution():
    """James buys 100 tennis balls and gives half of them away. The other half he puts into 5 large containers. How many tennis balls go in each container?"""
    # Define the number of tennis balls James buys and gives away
    total_balls = 100
    given_away = total_balls / 2

    # Calculate the number of tennis balls in each container
    balls_per_container = (total_balls - given_away) / 5

    # Display the number of tennis balls in each container
    result = balls_per_container
    return result

print(solution())