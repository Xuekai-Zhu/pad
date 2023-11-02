def solution():
    tank_capacity = 600
    bucket_capacity = 5
    jack_buckets_per_trip = 2
    jill_buckets_per_trip = 1
    jack_trip_ratio = 3/2

    # Calculate the number of total trips needed to fill the tank
    total_buckets_needed = tank_capacity / bucket_capacity
    total_trips_needed = total_buckets_needed / (jack_buckets_per_trip + jill_buckets_per_trip)

    # Calculate the number of trips Jack and Jill will make
    num_jack_trips = total_trips_needed * jack_trip_ratio
    num_jill_trips = total_trips_needed - num_jack_trips

    result = num_jill_trips
    return result

print(solution())