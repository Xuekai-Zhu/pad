def solution():
    # Define the number of times Billy rode his bike
    billy_rides = 17

    # Define the number of times John rode his bike
    john_rides = 2 * billy_rides

    # Define the number of times their mother rode her bike
    mother_rides = john_rides + 10

    # Calculate the total number of times they rode their bikes
    total_rides = billy_rides + john_rides + mother_rides
    result = total_rides
    return result

print(solution())