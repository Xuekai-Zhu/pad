def solution():
    total_water_needed = 600
    bucket_size = 5

    # Define the number of trips Jack can make in the time it takes Jill to make 2 trips
    jack_trips = 3
    jill_trips = 2

    # Define the amount of water each person can carry in one trip
    jack_water_per_trip = 2 * bucket_size
    jill_water_per_trip = bucket_size

    # Calculate the total water each person can carry in their allotted trips
    jack_total_water = jack_trips * jack_water_per_trip
    jill_total_water = jill_trips * jill_water_per_trip

    # Calculate the number of trips Jill needs to make to fill the remaining water needed
    remaining_water = total_water_needed - jack_total_water - jill_total_water
    jill_remaining_trips = remaining_water / bucket_size

    # Calculate the total number of trips Jill needs to make
    total_jill_trips = jill_trips + jill_remaining_trips
    result = total_jill_trips
    return result

print(solution())