def solution():
    """Jack and Jill went up the hill to fetch water to fill a 600 gallon tank. Each bucket is five gallons. Jack is stronger, and is able to carry two buckets of water at a time, but Jill can only manage one. Also, Jack can complete three trips to the well and back in the time it takes Jill to make two trips. How many trips will Jill make before the tank is filled?"""
    tank_capacity = 600
    bucket_capacity = 5
    jill_trip = 1
    jack_trip = 2
    jill_time = 2
    jack_time = 3

    # Calculate number of trips needed by Jack to fill the tank
    jack_trips = tank_capacity // (jack_trip * bucket_capacity)

    # Calculate number of trips needed by Jill to fill the tank
    jill_trips = (tank_capacity - jack_trips * jack_trip * bucket_capacity) // (
                jill_trip * bucket_capacity)

    result = jill_trips

    return result

print(solution())