def solution():
    playlist_time = 3 + 2 + 3  # Total time of Gabe's playlist is 8 minutes
    ride_time = 40  # Gabe's ride to the wrestling match is 40 minutes

    # Calculate the number of times Gabe can listen to his entire playlist on the ride
    times_on_ride = ride_time // playlist_time
    result = times_on_ride
    return result

print(solution())