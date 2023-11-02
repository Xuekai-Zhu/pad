def solution():
    """You walk twice as fast as Mr. Harris, and Mr. Harris took 2 hours to walk to the store. If your destination is 3 times further away than the store Mr. Harris walked to, how many hours will it take you to get there?"""
    mr_harris_time = 2
    your_speed = 2
    mr_harris_speed = 1
    store_distance = 1
    your_distance = 3 * store_distance
    your_time = your_distance / your_speed
    result = your_time
    return result

print(solution())