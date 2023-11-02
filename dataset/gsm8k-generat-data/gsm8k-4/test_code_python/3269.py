def solution():
    """A jug is filled with 5 liters of water and a bucket is filled with 4 jugs. How many liters of water are contained in 2 buckets?"""
    # Define the number of liters of water in a jug and a bucket
    jug_capacity = 5
    bucket_capacity = 4 * jug_capacity

    # Calculate the number of liters of water in 2 buckets
    total_water = 2 * bucket_capacity

    # Return the result
    result = total_water
    return result

print(solution())