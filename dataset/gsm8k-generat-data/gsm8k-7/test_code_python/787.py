def solution():
    eden_buckets = 4
    mary_buckets = eden_buckets + 3
    iris_buckets = mary_buckets - 1
    weight_per_bucket = 2

    # Calculate the total number of buckets of sand collected
    total_buckets = eden_buckets + mary_buckets + iris_buckets

    # Calculate the total weight of sand collected
    total_weight = total_buckets * weight_per_bucket
    result = total_weight
    return result

print(solution())