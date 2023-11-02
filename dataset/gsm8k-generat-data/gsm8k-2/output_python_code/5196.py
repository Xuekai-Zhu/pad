def solution():
    """If Billy rode his bike 17 times, John rode his bike twice as many times, and their mother rode her bike 10 times more than John, how many times did they ride their bikes in total?"""
    billy_rides = 17
    john_rides = 2 * billy_rides
    mother_rides = john_rides + 10
    total_rides = billy_rides + john_rides + mother_rides
    result = total_rides
    return result

print(solution())