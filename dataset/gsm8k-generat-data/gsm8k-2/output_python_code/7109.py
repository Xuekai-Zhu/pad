def solution():
    """Jack and Jill went up the hill to fetch water to fill a 600 gallon tank. Each bucket is five gallons. Jack is stronger, and is able to carry two buckets of water at a time, but Jill can only manage one. Also, Jack can complete three trips to the well and back in the time it takes Jill to make two trips. How many trips will Jill make before the tank is filled?"""
    tank_size = 600
    bucket_size = 5
    jack_carry = 2
    jill_carry = 1
    jack_time = 3
    jill_time = 2
    total_buckets = tank_size / bucket_size
    jack_buckets_per_trip = jack_carry * 2
    jill_buckets_per_trip = jill_carry * 1
    jack_trips_needed = total_buckets / jack_buckets_per_trip
    jill_trips_needed = (total_buckets - (jack_trips_needed * jack_buckets_per_trip)) / jill_buckets_per_trip
    total_time = (jack_trips_needed * jack_time) + (jill_trips_needed * jill_time)
    result = jill_trips_needed
    return result

print(solution())