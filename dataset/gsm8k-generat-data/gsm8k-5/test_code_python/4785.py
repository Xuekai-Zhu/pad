def solution():
    track_length = 0.25  # The length of the circular track is 1/4 mile
    lou_distance = 3  # Lou runs 3 miles on the track
    lou_laps = lou_distance / track_length  # Calculate the number of laps Lou runs
    rosie_speed = 2  # Rosie runs at twice the speed of Lou
    rosie_laps = (lou_distance * rosie_speed) / track_length  # Calculate the number of laps Rosie runs

    result = rosie_laps
    return result

print(solution())