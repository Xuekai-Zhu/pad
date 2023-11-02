def solution():
    # Calculate the time it takes to fill the pool with the bucket
    time_per_bucket = 20 # seconds
    bucket_size = 2 # gallons
    pool_size = 84 # gallons
    number_of_buckets = pool_size / bucket_size
    total_time = number_of_buckets * time_per_bucket

    # Convert the time from seconds to minutes
    time_in_minutes = total_time / 60
    result = time_in_minutes
    return result

print(solution())