def solution():
    """Jimmy wants to play in the inflatable swimming pool in his backyard. The swimming pool is empty and the garage is locked, so he cannot use the hose to fill the pool. He finds a 2 gallon bucket and calculates that it takes 20 seconds to fill the bucket from the tap and carry it to the pool where he pours in the water. If the pool holds 84 gallons of water, how many minutes will it take Jimmy to fill the pool?"""
    bucket_size = 2
    time_to_fill_bucket = 20
    pool_size = 84
    buckets_to_fill_pool = pool_size / bucket_size
    time_to_fill_pool_in_seconds = buckets_to_fill_pool * time_to_fill_bucket
    time_to_fill_pool_in_minutes = time_to_fill_pool_in_seconds / 60
    result = time_to_fill_pool_in_minutes
    return result

print(solution())