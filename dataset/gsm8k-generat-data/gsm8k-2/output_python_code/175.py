def solution():
    """Conner has a dune buggy that he rides in the desert. On flat sand, it can ride at a speed of 60 miles per hour. When traveling on downhill slopes, it can race at 12 miles per hour faster than it can when it is on flat sand. And when riding on an uphill inclined slow, it travels at a speed 18 miles per hour slower than when it is riding on flat sand. If Conner rides his dune buggy one-third of the time on flat sand, one-third of the time on uphill slopes, and one-third of the time on downhill slopes, what is his average speed in miles per hour?"""
    flat_sand_speed = 60
    downhill_speed = flat_sand_speed + 12
    uphill_speed = flat_sand_speed - 18
    flat_sand_time = 1/3
    downhill_time = 1/3
    uphill_time = 1/3
    total_distance = 100 # assume total distance covered to be 100 miles
    total_time = (flat_sand_time * total_distance / flat_sand_speed) + (downhill_time * total_distance / downhill_speed) + (uphill_time * total_distance / uphill_speed)
    avg_speed = total_distance / total_time
    result = avg_speed
    return result

print(solution())