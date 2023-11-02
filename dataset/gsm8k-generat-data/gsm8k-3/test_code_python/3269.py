def solution():
    """A jug is filled with 5 liters of water and a bucket is filled with 4 jugs. How many liters of water are contained in 2 buckets?"""
    # Define the volume of water in one jug
    JUG_VOLUME = 5

    # Define the number of jugs in one bucket
    JUGS_PER_BUCKET = 4

    # Calculate the volume of water in one bucket
    bucket_volume = JUG_VOLUME * JUGS_PER_BUCKET

    # Calculate the volume of water in two buckets
    total_volume = bucket_volume * 2

    # Display the total volume of water
    result = total_volume
    return result

print(solution())