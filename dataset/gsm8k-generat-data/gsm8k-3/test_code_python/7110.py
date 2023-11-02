def solution():
    """Jack and Jill went up the hill to fetch water to fill a 600 gallon tank. Each bucket is five gallons. Jack is stronger, and is able to carry two buckets of water at a time,
        but Jill can only manage one. Also, Jack can complete three trips to the well and back in the time it takes Jill to make two trips. How many trips will Jill make before the tank is filled?"""
    # Total gallons in the tank
    tank_capacity = 600

    # Gallon per bucket
    gallon_per_bucket = 5

    # Jack's efficiency
    jack_efficiency = 2

    # Jill's efficiency
    jill_efficiency = 1

    # Jack's time taken for 3 trips
    jack_time = 3

    # Jill's time taken for 2 trips
    jill_time = 2

    # Jack's capacity in a single trip
    jack_capacity = jack_efficiency * gallon_per_bucket

    # Gallons of water Jack can fill in 3 trips
    jack_gallons = jack_capacity * 3

    # Jill's capacity in a single trip
    jill_capacity = jill_efficiency * gallon_per_bucket

    # Time taken by Jack
    jack_fill_time = jack_time * jack_capacity

    # Time taken by Jill
    jill_fill_time = jill_time * jill_capacity

    # Jill's gallons of water filled in jill_time
    jill_gallons = jill_fill_time * (tank_capacity - jack_gallons) / (jack_fill_time + jill_fill_time)

    # Number of trips for Jill
    trips_jill = jill_gallons / jill_capacity

    # Display the number of trips Jill will make
    result = trips_jill
    return result

print(solution())