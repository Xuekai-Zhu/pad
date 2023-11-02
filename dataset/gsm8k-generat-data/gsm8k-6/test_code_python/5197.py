def solution():
    # Calculate the number of times Billy, John, and their mother rode their bikes
    billy_rides = 17
    john_rides = billy_rides * 2
    mother_rides = john_rides + 10

    # Calculate the total number of times they rode their bikes
    total_rides = billy_rides + john_rides + mother_rides
    result = total_rides
    return result

print(solution())