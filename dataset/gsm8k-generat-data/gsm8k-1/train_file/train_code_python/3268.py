def solution():
    """A jug is filled with 5 liters of water and a bucket is filled with 4 jugs. How many liters of water are contained in 2 buckets?"""
    liters_per_jug = 5
    jugs_per_bucket = 4
    jugs_in_two_buckets = 8
    total_liters = liters_per_jug * jugs_per_bucket * jugs_in_two_buckets
    result = total_liters
    return result

print(solution())