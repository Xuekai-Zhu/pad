def solution():
    """Conner has a dune buggy that he rides in the desert. On flat sand, it can ride at a speed of 60 miles per hour. When traveling on downhill slopes, it can race at 12 miles per hour faster than it can when it is on flat sand. And when riding on an uphill inclined slow, it travels at a speed 18 miles per hour slower than when it is riding on flat sand. If Conner rides his dune buggy one-third of the time on flat sand, one-third of the time on uphill slopes, and one-third of the time on downhill slopes, what is his average speed in miles per hour?"""
    time_on_flat_sand = 1/3
    time_on_downhill_slopes = 1/3
    time_on_uphill_slopes = 1/3
    speed_on_flat_sand = 60
    speed_on_downhill_slopes = speed_on_flat_sand + 12
    speed_on_uphill_slopes = speed_on_flat_sand - 18
    average_speed = (time_on_flat_sand * speed_on_flat

print(solution())