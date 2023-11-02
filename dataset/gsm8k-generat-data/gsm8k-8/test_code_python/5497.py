def solution():
    # Define the volume of the bucket and the pool
    bucket_volume = 2
    pool_volume = 84

    # Calculate the number of buckets Jimmy needs to fill the pool
    num_buckets = pool_volume / bucket_volume

    # Calculate the time it takes to fill and carry one bucket
    fill_time = 20

    # Calculate the total time to fill the pool
    total_time = num_buckets * fill_time

    # Convert the time to minutes
    total_time_in_minutes = total_time / 60
    result = total_time_in_minutes
    return result

print(solution())