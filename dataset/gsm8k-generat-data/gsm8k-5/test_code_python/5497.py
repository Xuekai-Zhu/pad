def solution():
    bucket_size = 2  # Jimmy uses a 2-gallon bucket
    time_per_bucket = 20  # Jimmy takes 20 seconds to fill the bucket and carry it to the pool
    pool_capacity = 84  # The swimming pool holds 84 gallons of water

    # Calculate how many buckets Jimmy needs to fill the pool
    buckets_needed = pool_capacity / bucket_size

    # Calculate the total time it will take Jimmy to fill the pool
    total_time = buckets_needed * time_per_bucket

    # Convert the total time to minutes
    minutes = total_time / 60
    result = minutes
    return result

print(solution())