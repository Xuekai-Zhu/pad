def solution():
    eden_buckets = 4  # Eden carried 4 buckets of sand
    mary_buckets = eden_buckets + 3  # Mary carried 3 more buckets of sand than Eden
    iris_buckets = mary_buckets - 1  # Iris carried 1 less bucket of sand than Mary
    bucket_weight = 2  # Each bucket contains 2 pounds of sand

    # Calculate the total weight of sand collected
    total_weight = (eden_buckets + mary_buckets + iris_buckets) * bucket_weight
    result = total_weight
    return result

print(solution())