def solution():
    billy_rides = 17  # Billy rode his bike 17 times
    john_rides = 2 * billy_rides  # John rode his bike twice as many times as Billy
    mother_rides = john_rides + 10  # Their mother rode her bike 10 times more than John

    # Calculate the total number of times they rode their bikes
    total_rides = billy_rides + john_rides + mother_rides
    result = total_rides
    return result

print(solution())