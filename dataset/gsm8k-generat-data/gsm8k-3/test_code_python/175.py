def solution():
    """Conner has a dune buggy that he rides in the desert. On flat sand, it can ride at a speed of 60 miles per hour. When traveling on downhill slopes, it can race at 12 miles per hour faster than it can when it is on flat sand. And when riding on an uphill inclined slow, it travels at a speed 18 miles per hour slower than when it is riding on flat sand. If Conner rides his dune buggy one-third of the time on flat sand, one-third of the time on uphill slopes, and one-third of the time on downhill slopes, what is his average speed in miles per hour?"""
    # Define the speed on flat sand, and the speed differences on uphill and downhill slopes
    FLAT_SPEED = 60
    UPHILL_DIFFERENCE = -18
    DOWNHILL_DIFFERENCE = 12

    # Define the proportion of time spent on each terrain
    flat_proportion = 1/3
    uphill_proportion = 1/3
    downhill_proportion = 1/3

    # Calculate the weighted average speed
    weighted_speed = (
        flat_proportion * FLAT_SPEED + 
        uphill_proportion * (FLAT_SPEED + UPHILL_DIFFERENCE) + 
        downhill_proportion * (FLAT_SPEED + DOWNHILL_DIFFERENCE)
    )

    result = weighted_speed
    return result

print(solution())