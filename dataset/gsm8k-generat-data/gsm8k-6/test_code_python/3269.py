def solution():
    # Calculate the total liters of water
    liters_in_jug = 5
    jugs_in_bucket = 4
    liters_in_bucket = jugs_in_bucket * liters_in_jug
    liters_in_two_buckets = 2 * liters_in_bucket
    result = liters_in_two_buckets
    return result

print(solution())