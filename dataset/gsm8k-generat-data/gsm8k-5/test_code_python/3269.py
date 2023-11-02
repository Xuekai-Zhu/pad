def solution():
    water_per_jug = 5  # Each jug is filled with 5 liters of water
    jugs_per_bucket = 4  # Each bucket is filled with 4 jugs
    buckets = 2  # We want to know how many liters of water are in 2 buckets

    # Calculate the total amount of water in the 2 buckets
    total_water = water_per_jug * jugs_per_bucket * buckets
    result = total_water
    return result

print(solution())