def solution():
    water_per_jug = 5
    jugs_per_bucket = 4
    num_buckets = 2

    # Calculate the total amount of water in one bucket
    water_per_bucket = water_per_jug * jugs_per_bucket

    # Calculate the total amount of water in two buckets
    total_water = water_per_bucket * num_buckets
    result = total_water
    return result

print(solution())