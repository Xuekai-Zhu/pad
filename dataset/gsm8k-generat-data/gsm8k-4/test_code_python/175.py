def solution():
    """Conner has a dune buggy that he rides in the desert. On flat sand, it can ride at a speed of 60 miles per hour. When traveling on downhill slopes, it can race at 12 miles per hour faster than it can when it is on flat sand. And when riding on an uphill inclined slow, it travels at a speed 18 miles per hour slower than when it is riding on flat sand. If Conner rides his dune buggy one-third of the time on flat sand, one-third of the time on uphill slopes, and one-third of the time on downhill slopes, what is his average speed in miles per hour?"""
    # Define the speed on flat sand, downhill slopes, and uphill slopes
    flat_sand_speed = 60
    downhill_speed = flat_sand_speed + 12
    uphill_speed = flat_sand_speed - 18

    # Define the time spent on each type of terrain
    flat_sand_time = 1/3
    downhill_time = 1/3
    uphill_time = 1/3

    # Calculate the average speed
    average_speed = flat_sand_time * flat_sand_speed + downhill_time * downhill_speed + uphill_time * uphill_speed

    result = average_speed
    return result

print(solution())