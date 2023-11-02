def solution():
    num_cans = 28
    cans_per_trip = 4
    draining_time = 30
    walking_time = 10

    # Calculate the total number of trips Jerry needs to make
    num_trips = num_cans // cans_per_trip
    if num_cans % cans_per_trip != 0:
        num_trips += 1

    # Calculate the total time for draining and walking for all trips
    total_draining_time = num_trips * draining_time
    total_walking_time = num_trips * 2 * walking_time

    # Calculate the total time for throwing all cans away
    total_time = total_draining_time + total_walking_time
    result = total_time
    return result

print(solution())