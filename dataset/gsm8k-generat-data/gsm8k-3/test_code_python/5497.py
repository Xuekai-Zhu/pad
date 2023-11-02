def solution():
    """Jimmy wants to play in the inflatable swimming pool in his backyard. The swimming pool is empty and the garage is locked, so he cannot use the hose to fill the pool. He finds a 2 gallon bucket and calculates that it takes 20 seconds to fill the bucket from the tap and carry it to the pool where he pours in the water. If the pool holds 84 gallons of water, how many minutes will it take Jimmy to fill the pool?"""
    # Define the capacity of the bucket and the time it takes to fill the bucket
    BUCKET_CAPACITY = 2
    TIME_TO_FILL_BUCKET = 20  # seconds

    # Define the capacity of the pool
    POOL_CAPACITY = 84

    # Calculate the number of buckets required to fill the pool
    num_buckets = POOL_CAPACITY / BUCKET_CAPACITY

    # Calculate the total time required to fill the pool
    total_time = num_buckets * TIME_TO_FILL_BUCKET  # seconds

    # Convert the total time to minutes
    minutes = total_time / 60

    # Display the total time in minutes
    result = minutes
    return result

print(solution())