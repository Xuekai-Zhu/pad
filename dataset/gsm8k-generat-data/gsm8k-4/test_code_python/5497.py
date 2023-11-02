def solution():
    """Jimmy wants to play in the inflatable swimming pool in his backyard. The swimming pool is empty and the garage is locked, so he cannot use the hose to fill the pool. He finds a 2 gallon bucket and calculates that it takes 20 seconds to fill the bucket from the tap and carry it to the pool where he pours in the water. If the pool holds 84 gallons of water, how many minutes will it take Jimmy to fill the pool?"""
    # Define the size of the bucket and the time it takes to fill it
    bucket_size = 2
    fill_time = 20

    # Calculate the number of buckets needed to fill the pool
    num_buckets = 84 / bucket_size

    # Calculate the total time it takes to fill the pool
    total_time = num_buckets * fill_time

    # Convert the total time from seconds to minutes
    total_time_minutes = total_time / 60

    # Return the result rounded to 2 decimal places
    result = round(total_time_minutes, 2)
    return result

print(solution())