def solution():
    bucket_size = 2  # gallons
    time_to_fill_bucket = 20  # seconds
    pool_capacity = 84  # gallons

    # Calculate the number of buckets needed to fill the pool
    num_buckets = pool_capacity / bucket_size

    # Calculate the total time needed to fill the pool in seconds
    total_time = num_buckets * time_to_fill_bucket

    # Convert the total time to minutes
    total_time_minutes = total_time / 60

    result = total_time_minutes
    return result

print(solution())