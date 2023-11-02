def solution():
    """A jug is filled with 5 liters of water and a bucket is filled with 4 jugs. How many liters of water are contained in 2 buckets?"""
    water_in_jug = 5
    jugs_in_bucket = 4
    water_in_bucket = jugs_in_bucket * water_in_jug
    buckets = 2
    total_water = buckets * water_in_bucket
    result = total_water
    return result

print(solution())