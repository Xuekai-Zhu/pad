def solution():
    """If Billy rode his bike 17 times, John rode his bike twice as many times, and their mother rode her bike 10 times more than John, how many times did they ride their bikes in total?"""
    # Define the number of times Billy rode his bike
    billy_rides = 17

    # Define the number of times John rode his bike
    john_rides = billy_rides * 2

    # Define the number of times their mother rode her bike
    mother_rides = john_rides + 10

    # Calculate the total number of times they rode their bikes
    total_rides = billy_rides + john_rides + mother_rides

    # return the result
    result = total_rides
    return result

print(solution())