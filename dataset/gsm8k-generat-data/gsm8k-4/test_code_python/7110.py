def solution():
    """Jack and Jill went up the hill to fetch water to fill a 600 gallon tank. Each bucket is five gallons. Jack is stronger, and is able to carry two buckets of water at a time, but Jill can only manage one. Also, Jack can complete three trips to the well and back in the time it takes Jill to make two trips. How many trips will Jill make before the tank is filled?"""
    # Define the total capacity of the tank and the capacity of each bucket
    tank_capacity = 600
    bucket_capacity = 5

    # Define the number of buckets carried by Jack and Jill
    jack_buckets = 2
    jill_buckets = 1

    # Define the time ratio between Jack and Jill
    jack_time_ratio = 3
    jill_time_ratio = 2

    # Calculate the total number of trips needed to fill the tank
    total_trips = tank_capacity / bucket_capacity

    # Calculate the number of trips made by Jack in the time it takes Jill to make one trip
    jack_trips = total_trips / (jack_time_ratio + jill_time_ratio * 2)

    # Calculate the number of trips made by Jill
    jill_trips = total_trips - jack_trips * jack_time_ratio

    result = jill_trips
    return result

print(solution())