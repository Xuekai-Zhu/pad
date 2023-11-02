def solution():
    """Jimmy wants to play in the inflatable swimming pool in his backyard. The swimming pool is empty and the garage is locked, so he cannot use the hose to fill the pool. He finds a 2 gallon bucket and calculates that it takes 20 seconds to fill the bucket from the tap and carry it to the pool where he pours in the water. If the pool holds 84 gallons of water, how many minutes will it take Jimmy to fill the pool?"""
    bucket_size = 2
    bucket_time = 20
    pool_size = 84
    gallons_per_bucket = bucket_size / 60
    time_per_bucket = bucket_time / 60
    buckets_needed = pool_size / bucket_size
    time_needed = buckets_needed * (time_per_bucket + (2 / gallons_per_bucket))
    result = time_needed
    return result

print(solution())